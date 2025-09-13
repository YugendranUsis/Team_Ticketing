frappe.listview_settings['Tickets'] = {
	refresh: function(listview) {
	   	// $("use.like-icon").hide();
        // $(".comment-count").hide();
	    // $(".frappe-timestamp").hide();
	    // $(".avatar-small").hide();
        // var count=0;
        // document.querySelectorAll('.list-row-col').forEach(function(col){
            
            
        //     col.style.minWidth='120px';
        //     col.style.maxWidth='120px';
        //     if(count==2){
        //        col.style.minWidth='300px';
        //     }
        //     count++;
        //     if(count==5){
        //         count=0;
        //     }

        // })
        
        //  document.querySelectorAll('.list-subject').forEach(function(col){
        //     col.style.minWidth='150px';
        //     col.style.maxWidth='150px';
            
            
            
        // })

        // let main_container=document.querySelector('.result')
        // if(main_container){
        //     main_container.style.overflowX='scroll';
        // }

        // document.querySelectorAll('.list-row-container').forEach(function(col){
        //     col.style.width='max-content';
        // })
        // document.querySelectorAll('.list-row-head').forEach(function(col){
        //     col.style.width='max-content';
        // })

        // document.querySelectorAll('.list-row .level-right').forEach(function(col){
        //     col.style.flex='0';
        // })

        // let ws = localStorage.getItem("current_page");
        // if (ws) {
        //     // Replace breadcrumbs manually
        //     frappe.breadcrumbs.clear();
        //     frappe.breadcrumbs.add(ws, frm.doctype, frm.docname);
        //     frappe.breadcrumbs.update();
        // }
        listview.page.wrapper.find('.list-row-col[data-fieldname="name"]').css({
            "flex": "0 0 80px",
            "max-width": "80px"
        });
        setTimeout(() => {
            $(".dropdown-menu .menu-item-label").each(function() {
                let allowed = ["Edit", "Export", "Delete"];
                let label = $(this).attr("data-label");

                // If this item is not allowed → remove its <li>
                if (!allowed.includes(label)) {
                    $(this).closest("li").remove();
                }
            });
        }, 500);
	}

};
