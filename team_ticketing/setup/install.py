import frappe
from frappe.core.doctype.file.file import File

def after_install():
    # Disable all default workspaces
    frappe.db.sql("""UPDATE `tabWorkspace` SET public=0 WHERE module != 'Team Ticketing'""")

    # Or delete them if you don’t want at all
    # frappe.db.sql("""DELETE FROM `tabWorkspace` WHERE module NOT IN ('Team Ticketing')""")

    frappe.clear_cache()
    update_website_settings()
    # stop_jobs_except_whitelist()
    hide_navbar_items()
    hide_doctype_global_search()
    # delete_all_departments()
    disable_roles()

#Update the Website Settings and System Settings
def update_website_settings():
    # Paths to your app's public images
    base_path = "/assets/team_ticketing/images"

    # Values to enforce
    updates = {
        "splash_image": f"{base_path}/logo.png",
        "app_logo": f"{base_path}/logo.png",
        "favicon": f"{base_path}/favicon.ico",
        "app_name": "Team Ticketing",
        "banner_image": f"{base_path}/logo.png",
        "copyright": "© 2025 Kodivian Technologies",
        "footer_powered": "Powered by Kodivian Technologies",
        "brand_html": "<img src='/assets/team_ticketing/images/logo.png'>",
        "hide_footer_signup": 0,
        "title_prefix": "Team Ticketing"
    }

    ws = frappe.get_single("Website Settings")

    # Always overwrite (insert if empty, update if present)
    for field, value in updates.items():
        ws.set(field, value)

    ws.save(ignore_permissions=True)
    frappe.db.commit()


    # Load System Settings (single DocType)
    ss = frappe.get_doc("System Settings")

    # Example: update values
    ss.email_footer_address = "Kodivian Pvt Ltd"   # remove ERPNext footer
    ss.disable_standard_email_footer=1
    ss.hide_footer_in_auto_email_reports=1
    ss.login_with_email_link=0
    ss.minimum_password_score=3
    ss.password_reset_limit=100
    ss.disable_system_update_notification=1
    ss.link_field_results_limit=50

    # Save changes
    ss.flags.ignore_mandatory = True
    ss.save(ignore_permissions=True)

    frappe.db.commit()


# we can set hide the unwanted doctypes in search
def hide_doctype_global_search():
    allow_search_doctypes = ["Employee", "Customers", "Projects","Department","Tickets"]
    doctypes = frappe.get_all("DocType", filters={"istable": 0}, pluck="name")

    for doctype in doctypes:
        if doctype not in allow_search_doctypes:
            frappe.db.set_value("DocType", doctype, "read_only", 1)


#This We Need to Set the upload the images public when we setup the installation
class CustomFile(File):
    def before_insert(self):
        super().before_insert()
        # Force all Website Settings uploads to be public
        if self.attached_to_doctype == "Website Settings":
            self.is_private = 0


#Stop the Unwanted the Scheduled Jobs
# def stop_jobs_except_whitelist():
#     # jobs you want to keep running
#     whitelist = [
#         "auto_email_report.send_monthly",
#         "backups.delete_downloadable_backups",
#         "deferred_insert.save_to_db",
#         "document_follow.send_hourly_updates",
#         "email_account.notify_unreplied",
#         "email_account.pull",
#         "email_digest.send",
#         "energy_point_log.send_monthly_summary",
#         "global_search.sync_global_search",
#         "google_calendar.sync",
#         "monitor.flush",
#         "notifications.clear_notifications",
#         "oauth.delete_oauth2_data",
#         "personal_data_deletion_request.process_data_deletion_request",
#         "prepared_report.expire_stalled_report",
#         "queue.flush",
#         "sessions.clear_expired_sessions",
#         "twofactor.delete_all_barcodes_for_users",
#         "user_settings.sync_user_settings",
#         "web_page.check_publish_status",
#     ]

#     jobs = frappe.get_all("Scheduled Job Type", fields=["name", "method", "stopped"])

#     for job in jobs:
#         if job.method not in whitelist:
#             doc = frappe.get_doc("Scheduled Job Type", job.name)
#             if not doc.stopped:
#                 doc.stopped = 1
#                 doc.save()
#                 frappe.db.commit()
#                 frappe.logger().info(f"Stopped job: {doc.method}")
#         else:
#             frappe.logger().info(f"Kept running: {job.method}")

#this usedto hidden the unwanted things in navbar 
def hide_navbar_items():
    settings = frappe.get_single("Navbar Settings")

    for item in settings.settings_dropdown:
        if item.item_label not in ["About", "Log out", "Reload", "Toggle Theme"]:
            item.hidden = 1

    settings.save(ignore_permissions=True)
    frappe.db.commit()  # optional, safe to leave

    for item in settings.help_dropdown:
        if item.item_label not in ["About", "Log out", "Reload", "Toggle Theme"]:
            item.hidden = 1

    settings.save(ignore_permissions=True)
    frappe.db.commit()  # optional, safe to leave

#this will delete all department so we can configure from scratch
# def delete_all_departments():
#     departments = frappe.get_all("Department", pluck="name")
#     for dept in departments:
#         frappe.delete_doc("Department", dept, force=True, ignore_permissions=True)
#     frappe.db.commit()

def disable_roles():
    # List of roles you want to keep enabled
    allowed_roles = ["Administrator","Admin","Ticket Manager","Supporting staff","HOD","Employee","System Manager","HR User"] 

    # Get all roles in the system
    all_roles = frappe.get_all("Role", fields=["name"])

    for role in all_roles:
        if role.name not in allowed_roles:
            # Disable role
            frappe.db.set_value("Role", role.name, "disabled", 1)

    frappe.db.commit()
