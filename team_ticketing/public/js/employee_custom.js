frappe.ui.form.on("Employee", {
    refresh: function(frm) {
    frm.set_df_property('naming_series', 'hidden', 1);
    setTimeout(() => {
            $('#form-tabs').css("display", "none");
        }, 100);
    $('[data-fieldname="naming_series"]').hide();
    }
});