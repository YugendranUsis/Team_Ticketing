// Copyright (c) 2025, Yugendran and contributors
// For license information, please see license.txt

frappe.ui.form.on("Tickets", {
	refresh(frm) {
		//Get The  Current User ID
		let current_user = frappe.session.user;

		//Based on Current User Set The Values User name,User Email,User Department
        if (!frm.doc.user_name) {  // Run only if user_name is empty or null
			frappe.call({
				method: "frappe.client.get_list",
				args: {
					doctype: "Employee",
					fields: ["employee_name", "user_id", "department"],
					filters: {
						user_id: current_user
					},
					limit_page_length: 1
				},
				callback: function (r) {
					if (r.message && r.message.length > 0) {
						let emp = r.message[0];
						frm.set_value("user_name", emp.employee_name);
						frm.set_value("user_email_id", emp.user_id);
						frm.set_value("user_department", emp.department);

					} else {
						frappe.msgprint("No matching Employee record found for the logged-in user.");
					}
				}
			});
		}

		if (frm.doc.workflow_state == "Resolved" ) {
			if (frm.doc.owner == current_user) {
				// Only owner: allow editing ticket_resolution_confirmation
				frm.fields_dict && Object.keys(frm.fields_dict).forEach(function(fieldname) {
					frm.set_df_property(fieldname, 'read_only', fieldname !== "ticket_resolution_confirmation" ? 1 : 0);
				});
			} else {
				// Not owner: all fields read-only
				frm.fields_dict && Object.keys(frm.fields_dict).forEach(function(fieldname) {
					frm.set_df_property(fieldname, 'read_only', 1);
				});
			}
		}
		setTimeout(()=>{
			$('.page-icon-group.hidden-xs.hidden-sm, .menu-btn-group, .col-lg-2.layout-side-section ,.actions-btn-group, .btn-reset.sidebar-toggle-btn, .form-dashboard, .form-dashboard-headline').hide();
			}, 100);

        // fetch workflow transitions from backend
		if(!frm.is_new()){
			frappe.xcall("frappe.model.workflow.get_transitions", {
				doc: frm.doc
			}).then(transitions => {
				if (transitions && transitions.length) {
					transitions.forEach(t => {
						let $btn = frm.page.add_inner_button(__(t.action), () => {

							let process_action = () => {
								frappe.xcall("frappe.model.workflow.apply_workflow", {
									doc: frm.doc,
									action: t.action
								}).then(() => {
									frm.reload_doc();
								});
							};

							if (frm.is_dirty()) {
								// Save first, then process
								frm.save().then(() => {
									frappe.model.with_doc(frm.doc.doctype, frm.doc.name, () => {
										process_action();
									});
								});
							} else {
								// Directly process the workflow action
								process_action();
							}
						});

            // Button colors
						if (t.action === "Approve") {
                            $btn.removeClass("btn-default").addClass("btn-success");
                        }
                        if (t.action === "Reject") {
                            $btn.removeClass("btn-default").addClass("btn-danger");
                        }
                        if (t.action === "Revise") {
                            $btn.removeClass("btn-default").addClass("btn-warning");
                        }
                        if (t.action === "Resolved") {
                            $btn.removeClass("btn-default").addClass("btn-success");
                        }
                        if (t.action === "Escalate") {
                            $btn.removeClass("btn-default").addClass("btn-warning");
                        }
                        if (t.action === "Close Ticket") {
                            $btn.removeClass("btn-default").addClass("btn-danger");
                        }
					});
				}
			});

		}
       	//Date fields only showing the current date and future dates it shows some error so need to use in last refresh event
				frm.fields_dict.expected_date_of_resolution.datepicker.update({
			minDate: new Date(frappe.datetime.get_today())
			});

			frm.fields_dict.resolution_date_according_to_staff.datepicker.update({
			minDate: new Date(frappe.datetime.get_today())
			});
		},



    //Based On Department we Just show and setting the department and deparment users
	//Here we used API call get User based on Department
		onload: function(frm) {
			frm.set_query("assign_to_user", function() {
				return {
					query: "team_ticketing.team_ticketing.doctype.tickets.tickets.get_employees_by_department",
					filters: {
						department: frm.doc.assign_to_department || ""
					}
				};
			});

			// Hide specific fields when creating a new ticket
			if (frm.is_new()) {
            let fields_to_hide = ['supporting_staff_resolution_confirmation','supporting_staff_resolution_confirmation','ticket_acceptance','reason_for_rejection','required_more_information','resolution_date_according_to_staff','supporting_staff_resolution_confirmation', 'resolution_notes', 'escalation_reason','department_head_action','resolution_comments','closure_comments'];
					fields_to_hide.forEach(field => {
						frm.set_df_property(field, 'hidden', true);
					});
            }
    },

	//this set assigner user in suport_staff name
	assign_to_user: function(frm) {
		if (frm.doc.assign_to_user) {
			console.log("Assign to user changed:", frm.doc.assign_to_user);
			frappe.call({
				method: "team_ticketing.team_ticketing.doctype.tickets.tickets.get_employee_name",
				args: {
					emp_id: frm.doc.assign_to_user
				},
				callback: function(r) {
					if (r.message && r.message.employee_name) {
						console.log("Employee found via API:", r.message.employee_name);
						frm.set_value("support_staff_name", r.message.employee_name);
						frm.refresh_field("support_staff_name");
					} else {
						frm.set_value("support_staff_name", "");
					}
				}
			});
		} else {
			frm.set_value("support_staff_name", "");
		}
	},
	// Refresh link field when department changes
    assign_to_department: function(frm) {
        // Step 1: Clear the assign_to_user field
        frm.set_value("assign_to_user", "");
        frm.refresh_field("assign_to_user");
        frappe.call({
            method: "team_ticketing.team_ticketing.doctype.tickets.tickets.get_department_head",
            args: { department: frm.doc.assign_to_department },
            callback: function(r) {
                console.log("Server response:", r);
                if (r && r.message) {
                    frm.set_value(
                        "assigned_department_head",
                        r.message.name
                    );
                } else {
                    frm.set_value("assigned_department_head", "");
                }
            }
        });

    },

});




// function get_action_style(action) {
//     switch(action.toLowerCase()) {
//         case "approve": return "btn-success";   // green
//         case "reject": return "btn-danger";    // red
//         case "revise": return "btn-warning";   // yellow
//         default: return "btn-secondary";
//     }
// }



// if(frm.doc.workflow_state != "Created" || frm.doc.ticket_acceptance != "Revise"){
// 				fields=["ticket_title","ticket_description","expected_date_of_resolution","priority","assign_to_department","assign_to_user","attachment"]
// 				for(field in fields){
// 					frm.toggle_enable(field, false);
// 					console.log("Working")
// 					frm.set_df_property(field, 'read_only', 1);
// 					frm.refresh_field(field);


// 					console.log("Working")
// 				}
// 			}
// eval:(!doc.__islocal && doc.owner == session.user && doc.ticket_acceptance != "Revise" || doc.workflow_state != "Created")
