# Copyright (c) 2025, Yugendran and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Tickets(Document):
    def validate(self):
        if self.ticket_acceptance == "Reject":
            if not self.reason_for_rejection:
                frappe.throw("Reason for Rejection is mandatory when ticket is rejected.")

        if self.ticket_acceptance == "Revise":
            if not self.required_more_information:
                frappe.throw("Required More Information is mandatory when ticket is revised.")

        if self.ticket_acceptance == "Approve":
            if not self.resolution_date_according_to_staff:
                frappe.throw("Resolution Date According to Staff is mandatory when ticket is accepted.")

        if self.supporting_staff_resolution_confirmation=="Resolved":
            if not self.resolution_notes:
                frappe.throw("Resolution notes is mandatory when ticket is Resolved.")

        if self.supporting_staff_resolution_confirmation=="Escalated":
            if not self.escalation_reason:
                frappe.throw("Escalation reason is mandatory when ticket is Escalated.")

        if self.department_head_action=="Ticket Closed":
            if not self.closure_comments:
                frappe.throw("Closure Comments is mandatory when ticket is Closed.")

        if self.workflow_state=="Resolved" and self.supporting_staff_resolution_confirmation=="Escalated":
            if not self.resolution_comments:
                frappe.throw("Resolution comments is mandatory when ticket is Resolved.")
            else:
                self.department_head_action="Resolved"

        if self.workflow_state=="Acknowledged":
            if not self.ticket_resolution_confirmation  :
                frappe.throw("Ticket Resolution Confirmation is mandatory when ticket is Acknowledged.")

    def on_update(self):
        # Only send when it CHANGES to "Submitted"
        if self.workflow_state == "Submitted" and self.get_doc_before_save():
            old_state = self.get_doc_before_save().workflow_state
            if old_state != "Submitted":  # state changed
                send_ticket_notification(self)

def has_permission(doc, user=None):
    # Always allow checking, actual filter happens in query
    return True

def get_permission_query_conditions(user):
    if not user:
        user = frappe.session.user

    #Show All Records to Admin and Sysmanger Role and Ticket Manager
    if user == "Administrator" or {"System Manager","Ticket Manager"} & set(frappe.get_roles(user)):
        return ""

    # Get employee info linked to current user
    employee = frappe.db.get_value(
        "Employee",
        {"user_id": user},
        ["name", "department", "custom_department_head"],
        as_dict=True
    )

    # No Employee record → only allow their own tickets (by owner)
    if not employee:
        return f"""`tabTickets`.`owner` = '{user}'"""

    roles = frappe.get_roles(user)
    print(roles)

    # Department Head → see all tickets in department OR tickets they created
    if employee.custom_department_head:
        return f"""(`tabTickets`.`assign_to_department` = '{employee.department}'
                    OR `tabTickets`.`owner` = '{user}')"""

    # # Supporting Staff → see their own tickets OR tickets they created
    if "Supporting Staff" in roles:
        return f"""(`tabTickets`.`assign_to_user` = '{employee.name}'
                    OR `tabTickets`.`owner` = '{user}')"""

    # Other users → see only their own tickets or ones assigned to them
    return f"""(`tabTickets`.`assign_to_user` = '{employee.name}'
                OR `tabTickets`.`owner` = '{user}')"""


#THis API Used For Get Active Employee Based On Department
@frappe.whitelist()
def get_employees_by_department(doctype, txt, searchfield, start, page_len, filters):
    department = filters.get("department")
    if not department:
        return []

    # This ignores permissions completely
    employees = frappe.get_all(
        "Employee",
        fields=["name", "employee_name", "user_id"],
        filters={"department": department, "status": "Active"},
        ignore_permissions=True
    )
    Supporting_Employees=[]
    for emp in employees:
        if emp.user_id and frappe.db.exists("Has Role",{"Parent":emp.user_id,"role":"Supporting Staff"}):
            Supporting_Employees.append(emp)

    txt_lower = (txt or "").lower()
    filtered = [
        emp for emp in Supporting_Employees
        if txt_lower in emp.name.lower() or txt_lower in emp.employee_name.lower()
    ]

    # Frappe dropdown expects a list of tuples
    return [(emp.name, emp.employee_name) for emp in filtered]


#This API Used to Get Active Deparmtent Head Employee
@frappe.whitelist()
def get_department_head(department):
    if not department:
        return {}

    # try to find explicit department head
    heads = frappe.get_all(
        "Employee",
        fields=["name", "employee_name"],
        filters={"department": department, "custom_department_head": 1,"status": "Active" },
        limit=1,
        ignore_permissions=True
    )

    if heads:
        return heads[0]

    # fallback: return first Active employee in department
    # employees = frappe.get_all(
    #     "Employee",
    #     fields=["name", "employee_name"],
    #     filters={"department": department,"status": "Active" },
    #     limit=1,
    #     ignore_permissions=True
    # )
    # return employees[0] if employees else {}
    frappe.throw(f'HOD is not assigned for this {department} Department. Please Contact HR.')



@frappe.whitelist()
def get_employee_name(emp_id):
    # bypasses user permission restrictions
    emp_name = frappe.db.get_value("Employee", emp_id, "employee_name")
    return {"employee_name": emp_name}


#This Part is for Email Notification send when Ticket is create New
# class Ticket(Document):
#     def after_insert(self):
#         """Trigger email after ticket is created."""
#         send_ticket_notification(self)

def send_ticket_notification(doc):
    # 1. Get Assigned Department Head Employee ID
    department_head_emp_id = doc.assigned_department_head  # Link to Employee

    if not department_head_emp_id:
        frappe.log_error("No department head assigned for ticket", "Ticket Notification")
        return

    # 2. Get user_id from Employee (usually maps to a User ID)
    user_id = frappe.db.get_value("Employee", department_head_emp_id, "user_id")
    print(user_id)
    if not user_id:
        frappe.log_error(f"No user_id found for Employee: {department_head_emp_id}", "Ticket Notification")
        return

    # 3. Get actual email address from User doctype
    email = frappe.db.get_value("User", user_id, "email")
    print(email)
    if not email:
        frappe.log_error(f"No email found for User: {user_id}", "Ticket Notification")
        return
    if doc.attachment:
        file_doc = frappe.get_doc("File", {"file_url": doc.attachment})
        file_url = frappe.utils.get_url(doc.attachment)
        file_content = file_doc.get_content()
    # 4. Send the email
    subject = f"New Ticket Assigned: {doc.name}"
    message = f"""
        Dear Department Head,<br><br>
        A new ticket <b>{doc.name}</b> has been assigned.<br><br>
        <b>Subject:</b> {doc.ticket_title}<br>
        <b>Description:</b> {doc.ticket_description}<br>
        <b>Priority:</b> {doc.priority}<br><br>
        Regards,<br>
        Supporting Team
    """
    if doc.attachment:
        frappe.sendmail(
            recipients=[email],
            cc=["yugendran@usistech.com"],
            subject=subject,
            message=message,
            attachments=[{
                "fname": file_doc.file_name,
                "fcontent": file_content,
                "content_id": "attached_img"
            }]
        )
    else:
        frappe.sendmail(
            recipients=[email],
            cc=["yugendran@usistech.com"],
            subject=subject,
            message=message
        )


    frappe.logger().info(f"Ticket notification sent to {email}")



@frappe.whitelist()
def get_required_fields(doctype, action, state=None):
    # check by (action + state)
    if state and (action, state) in action_field_map:
        return action_field_map[(action, state)]

    # fallback
    return []



action_field_map = {
    ("Approve", "Submitted"): [
        {"fieldname": "resolution_date_according_to_staff", "fieldtype": "Date", "label": "Resolution Date According to Staff", "reqd": 1}
    ],
    ("Reject", "Submitted"): [
        {"fieldname": "reason_for_rejection", "fieldtype": "Small Text", "label": "Reason for Rejection", "reqd": 1}
    ],
    ("Revise", "Submitted"): [
        {"fieldname": "required_more_information", "fieldtype": "Small Text", "label": "Required More Information", "reqd": 1}
    ],
    ("Resolved", "Approve"): [
        {"fieldname": "resolution_notes", "fieldtype": "Small Text", "label": "Resolution Notes", "reqd": 1}
    ],
    ("Escalate", "Approve"): [
        {"fieldname": "escalation_reason", "fieldtype": "Small Text", "label": "Escalation Reason", "reqd": 1}
    ],
    ("Resolved", "Escalated"): [
        {"fieldname": "resolution_comments", "fieldtype": "Small Text", "label": "Resolution Comments", "reqd": 1}
    ],
    ("Close Ticket", "Escalated"): [
        {"fieldname": "closure_comments", "fieldtype": "Small Text", "label": "Closure Comments", "reqd": 1}
    ],
    ("Acknowledge", "Resolved"): [
        {"fieldname": "ticket_resolution_confirmation", "fieldtype": "Check", "label": "Ticket Resolution Confirmation", "reqd": 1}
    ],
}
