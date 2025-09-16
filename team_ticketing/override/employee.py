import frappe
from frappe.model.naming import make_autoname
from erpnext.hr.doctype.employee.employee import Employee as ERPNextEmployee

class Employee(ERPNextEmployee):
    def autoname(self):
        # Custom Employee ID series: EMP0001, EMP0002, ...
        self.name = make_autoname("EMP#####")
