

from project.settings.config.main.naming import COMPANY_NAME, PROJECT_SHORT_TITLE, PROJECT_TITLE


JAZZMIN_SETTINGS = {
    "site_title": PROJECT_SHORT_TITLE,
    "site_header": PROJECT_SHORT_TITLE,
    "site_brand": PROJECT_SHORT_TITLE,
    "site_logo": 'admin\img\logo.png',
    "login_logo": 'admin\img\logo-black.png',
    "login_logo_dark": 'admin\img\logo-white.png',
    "site_logo_classes": "img-circle",
    "site_icon": 'admin\img\\favicon.png',
    "welcome_sign": f'Welcome to {PROJECT_TITLE.title()}',
    "copyright": COMPANY_NAME,
    "search_model": ["auth.User", ],
    "user_avatar": 'True',
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {
            "name": "Home",
            "url": "admin:index",
            "permissions": ["auth.view_user"],
        },
        # external url that opens in a new window (Permissions can be added)
       
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "books"},
        {
            "name": "Support",
            "url": "https://www.buzzbites.in/contact",
            "new_window": True,
        },
    ],
    "usermenu_links": [
        # {
        #     "name": "Support",
        #     "url": "https://www.buzzbites.in/contact",
        #     "new_window": True,
        # },
        # {"model": "auth.user"},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [''],
    "hide_models": ['auth.group'],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    "custom_links": {
        # "books": [
        #     {
        #         "name": "Make Messages",
        #         "url": "make_messages",
        #         "icon": "fas fa-comments",
        #         "permissions": ["books.view_book"],
        #     }
        # ]
    },
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        # "App1.Customer": "fas fa-users",
        # "App1.Employee": "fas fa-users",
        # "App1.Announcements": "fas fa-bell",
        # "App1.Department": "fas fa-building",
        # "App1.MonthlyInstallment": "fas fa-coins",
        # "App1.compansation": "fas fa-handshake",
        # "App1.Administration": "fas fa-paperclip",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "custom_css": 'admin/css/custom.css',
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "language_chooser": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-info",
    "accent": "accent-lightblue",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-light-info",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "flatly",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": True
}