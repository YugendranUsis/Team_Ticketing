frappe.ui.toolbar.show_about = function() {
    let d = new frappe.ui.Dialog({
        title: __("About"),
        fields: [
            {
                fieldtype: "HTML",
                fieldname: "about_html",
                options: `
                    <div style="text-align: center; padding: 20px;">
                        <h2>Team Ticketing App</h2>
                        <p>Powered by Kodivian Framework</p>
                        <p>Version: 1.0.0</p>
                        <hr>
                        <p>For support contact: <a href="mailto:support@example.com">support@example.com</a></p>
                    </div>
                `
            }
        ]
    });
    d.show();
};


// frappe.provide("frappe.ui.misc");

// frappe.ui.misc.about = function() {
//     let d = new frappe.ui.Dialog({
//         title: __("About"),
//         fields: [
//             {
//                 fieldtype: "HTML",
//                 fieldname: "about_html",
//                 options: `
//                     <div style="text-align: center; padding: 20px;">
//                         <h2>Team Ticketing</h2>
//                         <p>Powered by Kodivian Framework</p>
//                         <p>Version: 2.0.0</p>
//                         <hr>
//                         <p>For support contact: <a href="mailto:support@example.com">support@example.com</a></p>
//                     </div>
//                 `
//             }
//         ]
//     });
//     d.show();
// };
