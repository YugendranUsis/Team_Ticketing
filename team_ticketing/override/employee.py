import frappe
from frappe.model.naming import make_autoname
from erpnext.setup.doctype.employee.employee import Employee as ERPNextEmployee

class Employee(ERPNextEmployee):
    def autoname(self):
        # Custom Employee ID series: EM.0001, EM.0002, ...
        self.name = make_autoname("EMP.#####")
