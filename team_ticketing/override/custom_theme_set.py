import frappe 

@frappe.whitelist()
def theme_switcher(theme):
    if theme in ["Dark","Light","Automatic"]:
        frappe.db.set_value("User",frappe.session.user,"desk_theme",theme)