import frappe
from frappe.model.naming import make_autoname
from erpnext.setup.doctype.department.department import Department as ERPNextDepartment

class Department(ERPNextDepartment):
    def autoname(self):
        # custom naming series: DEPT - 00001, DEPT - 00002...
        self.name = make_autoname("DEPT - .#####")
