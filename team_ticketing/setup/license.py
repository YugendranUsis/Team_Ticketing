import frappe
import requests
from frappe import _
from datetime import datetime

LICENSE_API_URL = "https://your-license-server.com/check_license"

def check_license():
    site_id = frappe.get_site_config().get("site_id")  # store unique ID in site_config.json
    if not site_id:
        frappe.throw(_("Site not registered. Contact vendor."))

    try:
        response = requests.post(LICENSE_API_URL, json={"site_id": site_id}, timeout=5)
        data = response.json()
        if not data.get("valid"):
            frappe.throw(_("Certificate expired or invalid. Contact vendor."))
    except Exception as e:
        frappe.throw(_("Cannot verify license: {}").format(str(e)))
