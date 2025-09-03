// frappe.ready(() => {
//     // Change desk top-left logo (navbar)
//     const brand = document.querySelector(".navbar-brand");
//     if (brand) {
//         const img = brand.querySelector("img");
//         if (img) {
//             img.src = "/assets/team_ticketing/images/logo.png";  // your logo
//             img.style.height = "24px";
//         }
//         brand.title = "Team Ticketing";   // tooltip
//         brand.innerHTML = `<img src="/assets/team_ticketing/images/logo.png" style="height:24px; margin-right:6px;"> `;
//     }
// });
// frappe.after_ajax && frappe.after_ajax(() => {
//     setTimeout(()=>{
//         $('.page-icon-group.hidden-xs.hidden-sm, .menu-btn-group, .col-lg-2.layout-side-section, .btn-reset.sidebar-toggle-btn').hide();
//     }, 100);
// });
// Prove the file loaded



// console.log("Team Ticketing hide_sidebar.js loaded");
//   const style = document.createElement("style");
//   style.textContent = `
//     .form-sidebar,
//     .layout-side-section,
//     .report-sidebar,
//     workspace-footer,
//     .menu-btn-group,
//     .standard-actions .flex {
//       display: none !important;  
//     }
//   `;
//   document.head.appendChild(style);



    // if (frappe.session.user !== "Administrator") {
    //     // Apply CSS to hide search bar
    //     const style = document.createElement("style");
    //     style.innerHTML = `
    //         .input-group.search-bar.text-muted {
    //             display: none !important;
    //         }
    //     `;
    //     document.head.appendChild(style);
    // }
