frappe.ui.form.on("Department",{
  refresh:function(frm){
        frm.set_df_property("approvers", "hidden", 1);
        frm.set_df_property("company", "hidden", 1);
        frm.set_df_property("expense_approvers", "hidden", 1);
        frm.set_df_property("is_group", "hidden", 1);
        frm.set_df_property("leave_approvers", "hidden", 1);
        frm.set_df_property("leave_block_list", "hidden", 1);
        frm.set_df_property("lft", "hidden", 1);
        frm.set_df_property("old_parent", "hidden", 1);
        frm.set_df_property("parent_department", "hidden", 1);
        frm.set_df_property("payroll_cost_center", "hidden", 1);
        frm.set_df_property("rgt", "hidden", 1);
        frm.set_df_property("shift_request_approver", "hidden", 1);
  }
});