//Hide the Search bar Except admin
frappe.after_ajax(() => {
    const current_user = frappe.boot?.user?.name || frappe.boot?.profile?.name || frappe.session.user;
    console.log("User:", current_user);
    //User name admin only
    if (current_user !== "Administrator") {
        const style = document.createElement("style");
        style.innerHTML = `
            .input-group.search-bar.text-muted {
                display: none !important;
            }
        `;
        document.head.appendChild(style);
    }

	//based on user role
	if (!frappe.user.has_role("System Manager")) {
        const style = document.createElement("style");
        style.innerHTML = `
            .input-group.search-bar.text-muted {
                display: none !important;
            }
        `;
        document.head.appendChild(style);
    }
});


