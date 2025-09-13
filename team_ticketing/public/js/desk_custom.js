//Hide the Search bar Except admin
frappe.after_ajax(() => {
setTimeout(() => {
    $(".dropdown-menu .menu-item-label[data-label='Print']").closest("li").remove();
    $(".dropdown-menu .menu-item-label[data-label='Add%20Tags']").closest("li").remove();
    $(".dropdown-menu .menu-item-label[data-label='Apply%20Assignment%20Rule']").closest("li").remove();
    $(".dropdown-menu .menu-item-label[data-label='Clear%20Assignment']").closest("li").remove();
    $(".dropdown-menu .menu-item-label[data-label='Assign%20To']").closest("li").remove();
    $(".dropdown-menu .menu-item-label[data-label='Export']").closest("li").remove();
    },500);
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


