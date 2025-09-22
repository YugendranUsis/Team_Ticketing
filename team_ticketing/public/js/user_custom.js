frappe.ui.form.on("User", {
    refresh: function(frm) {
        // hide the field
        frm.set_df_property("desk_settings_section", "hidden", 1);
        frm.set_df_property("list_settings_section", "hidden", 1);
        frm.set_df_property("form_settings_section", "hidden", 1);
        frm.set_df_property("document_follow_notifications_section", "hidden", 1);
        frm.set_df_property("email_settings", "hidden", 1);
        frm.set_df_property("app_section", "hidden", 1);
        frm.set_df_property("sb3", "hidden", 1);
        frm.set_df_property("third_party_authentication", "hidden", 1);
        frm.set_df_property("api_access", "hidden", 1);
        frm.set_df_property("navigation_settings_section", "hidden", 1);
        frm.set_df_property("sb3", "hidden", 1);
        frm.set_df_property("block_modules", "hidden", 1);
        frm.set_df_property("MultiCheck", "hidden", 1);
        setTimeout(() => {
            $('.custom-actions.hidden-xs.hidden-md').css("display", "none");
        }, 100);
        $('[data-fieldname="desk_settings_section"]').hide();
        $('[data-fieldname="sb3"]').hide();
        $('[data-fieldname="block_modules"]').hide();
        $('[data-fieldname="MultiCheck"]').hide();
        $('[data-fieldname="navigation_settings_section"]').hide();
        
        frm.set_query("default_workspace", function() {
                    return {
                        filters: {
                            module: "Team Ticketing"   // your custom module name
                        }
                    };
                });
        
        frm.set_query("role_profile_name", function() {
            return {
                filters: {
                    name: ["in", ["Admin", "Employee and HOD","Supporting Staff","Ticket manager","Employee"]]
                }
            };
        });
    }
});

frappe.ui.form.on("User", {
    onload_post_render: function(frm) {
        if (frm.fields_dict.role_profile_name) {
            frm.fields_dict.role_profile_name.get_query = function() {
                return {
                    filters: {
                        name: ["in", ["Admin", "Employee and HOD","Supporting Staff","Ticket manager","Employee"]]
                    }
                };
            };
        }
    }
});
