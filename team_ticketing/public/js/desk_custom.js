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


	const allowed_roles = ["System Manager", "HOD", "Ticket Manager"];
    const user_roles = frappe.boot.user.roles || [];
	console.log("User Roles:", user_roles);

    // Detect if current page is Report View
    // const in_report_view = window.location.pathname.includes("/app/tickets/view/report");

    // const toggle_menu_button = () => {
    //     const menu_btns = document.querySelectorAll(".menu-btn-group");
    //     menu_btns.forEach(el => {
    //         if (in_report_view && allowed_roles.some(r => user_roles.includes(r))) {
    //             el.style.display = "block";  // ✅ show in Report View for allowed roles
    //         } else {
    //             el.style.display = "none";   // 🚫 hide otherwise
    //         }
    //     });



    // };
	const toggle_menu_button = () => {
        const in_report_view = frappe.get_route_str().includes("tickets/view/report");
        const menu_btns = document.querySelectorAll(".menu-btn-group");

        menu_btns.forEach(el => {
            if (in_report_view && allowed_roles.some(r => user_roles.includes(r))) {
                el.style.display = "block";   // ✅ show in Report View for allowed roles
            } else {
                el.style.display = "none";    // 🚫 hide otherwise
            }
        });
    };

    // Run once initially
    toggle_menu_button();

    // Run on route change
    frappe.router.on("change", () => {
        setTimeout(toggle_menu_button, 300);
    });

    // Watch DOM changes (for view switches without reload)
    const observer = new MutationObserver(() => {
        toggle_menu_button();
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
});


