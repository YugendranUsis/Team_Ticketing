// Copyright (c) 2025, Yugendran and contributors
// For license information, please see license.txt

frappe.ui.form.on("Projects", {
	refresh(frm) {
     let ws = localStorage.getItem("current_page");
        if (ws) {
            // Replace breadcrumbs manually
            frappe.breadcrumbs.clear();
            frappe.breadcrumbs.add(ws, frm.doctype);
            frappe.breadcrumbs.update();
        }
	},
});
