frappe.ui.form.on("Employee", {
    refresh: function(frm) {
    setTimeout(() => {
            $('#form-tabs').css("display", "none");
        }, 100);
    }
});