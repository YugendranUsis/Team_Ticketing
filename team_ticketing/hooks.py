app_name = "team_ticketing"
app_title = "Team Ticketing"
app_publisher = "Yugendran"
app_description = "Team Ticketing"
app_email = "yugendran@usistech.com"
app_license = "mit"
home_page = "/app/dashboard/Team Ticketing"


# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "team_ticketing",
# 		"logo": "/assets/team_ticketing/logo.png",
# 		"title": "Team Ticketing",
# 		"route": "/team_ticketing",
# 		"has_permission": "team_ticketing.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

#The below JS used for updating the about pop up page
app_include_js = [
    "assets/team_ticketing/js/about.js",
    "/assets/team_ticketing/js/desk_custom.js",
]
# 
app_include_css = [
    "/assets/team_ticketing/css/custom.css",
]

website_context = { 
                   "splash_image": "/assets/team_ticketing/images/logo.png",
                   "favicon": "/assets/team_ticketing/images/logo.png",
                   "app_title": "Team Ticketing",
                   "app_name": "Team Ticketing",
                   "app_logo": "/assets/team_ticketing/images/logo.png",
                   "brand_html": '<img src="/assets/team_ticketing/images/logo.png" style="height: 24px; margin-right: 8px;">',

}


# include js, css files in header of desk.html
# app_include_css = "/assets/team_ticketing/css/team_ticketing.css"
# app_include_js = "/assets/team_ticketing/js/team_ticketing.js"

# include js, css files in header of web template
# web_include_css = "/assets/team_ticketing/css/team_ticketing.css"
# web_include_js = "/assets/team_ticketing/js/team_ticketing.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "team_ticketing/public/scss/theme_switch"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}


# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "team_ticketing/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "team_ticketing.utils.jinja_methods",
# 	"filters": "team_ticketing.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "team_ticketing.install.before_install"
after_install = "team_ticketing.setup.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "team_ticketing.uninstall.before_uninstall"
# after_uninstall = "team_ticketing.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "team_ticketing.utils.before_app_install"
# after_app_install = "team_ticketing.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "team_ticketing.utils.before_app_uninstall"
# after_app_uninstall = "team_ticketing.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "team_ticketing.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }
permission_query_conditions = {
    "Tickets": [
        "team_ticketing.team_ticketing.doctype.tickets.tickets.get_permission_query_conditions"
    ]
}

has_permission = {
    "Tickets": [
        "team_ticketing.team_ticketing.doctype.tickets.tickets.has_permission"
    ]
}




override_doctype_class = {
    "File": "team_ticketing.setup.install.CustomFile"
}


# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"team_ticketing.tasks.all"
# 	],
# 	"daily": [
# 		"team_ticketing.tasks.daily"
# 	],
# 	"hourly": [
# 		"team_ticketing.tasks.hourly"
# 	],
# 	"weekly": [
# 		"team_ticketing.tasks.weekly"
# 	],
# 	"monthly": [
# 		"team_ticketing.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "team_ticketing.install.before_tests"

#Branding
# app_logo = "/assets/team_ticketing/images/logo.png"
# app_icon = "octicon octicon-file-directory"
# app_color = "grey"
# app_title = "Team Ticketing"
# app_publisher = "Yugendran"
# app_description = "A custom app for managing team tickets"
# app_email = "Yugendran@usistech.com"
# app_version = "0.0.1"
# brand_html = '<img src="/assets/team_ticketing/images/logo.png" style="height: 20px;">'

# app_logo_url = "/assets/team_ticketing/images/logo.png"
# app_favicon = "/assets/team_ticketing/images/logo.png"

#Email Footer

# email_footer_address = "Kodivian Pvt Ltd"
default_mail_footer = """
 <div>
Kodivian Pvt Ltd
</div>
"""

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "team_ticketing.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "team_ticketing.task.get_dashboard_data"
# }

#This Used to Override the User Switch theme
# override_whitelisted_methods = {
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["team_ticketing.utils.before_request"]
# after_request = ["team_ticketing.utils.after_request"]

# Job Events
# ----------
# before_job = ["team_ticketing.utils.before_job"]
# after_job = ["team_ticketing.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"team_ticketing.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


########################################### FIXTURE BLOCK ################################################################


#Fixtures
# fixtures = [
#     #custom fields
#     {"dt": "Custom Field", "filters": [["name", "=", "Employee-custom_department_head"]]},

#     #workflow states and Action
#     {"dt": "Workflow", "filters": [["name", "=", "Team Ticketing"]]},
#     {
#         "doctype": "Workflow State",
#         "filters": [["name", "in", ["Created","Submitted", "Approve", "Revise","Reject","Resolved","Escalated","Ticket Closed","Acknowledged"]]]
#     },
#     {
#         "doctype": "Workflow Action Master",
#         "filters": [["name", "in", ["Submit","Approve", "Revise", "Reject","Resolved","Escalate","Close Ticket","Re Submit","Acknowledge"]]]
#     },
#     # Roles
#     {"dt": "Role", "filters": [["role_name", "in", ["HOD", "Ticket Manager", "Supporting staff"]]]},

#     #Module Profile
#      {"dt": "Module Profile", "filters": [["name", "in", ["Team Ticket"]]]},
#     # Role Profiles
#     {"dt": "Role Profile", "filters": [["name", "in", ["Employee and HOD", "Ticket manager","Supporting Staff","Employee"]]]},
#     {"dt": "Has Role", "filters": [["parent", "in", ["Employee and HOD", "Ticket manager","Supporting Staff","Employee"]]]},
#     # Custom DocPerms (Role Permissions Manager)
#     {
#         "dt": "Custom DocPerm",
#         "filters": [
#             ["parent", "in", [
#                 "Projects",
#                 "Tickets",
#                 "Customers",
#                 "Department",
#             ]]
#         ]
#     },
#  {"dt": "Custom HTML Block", "filters": [["name", "in", ["My Tickets", "Tickets Assigned To Me"]]]},
# ]
