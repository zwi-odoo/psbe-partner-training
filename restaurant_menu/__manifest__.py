{
    "name": "Restaurant Menu",
    "summary": """
        Training module designed for partner training - Simulating a restaurant
        """,
    "category": "",
    "version": "17.0.0.0.0",
    "author": "Odoo PS",
    "website": "https://www.odoo.com",
    "license": "OEEL-1",
    "depends": [
        "base",
    ],
    "data": [
        # SECURITY
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        # VIEWS
        "views/restaurant_menu_views.xml",
        "views/restaurant_menu_item_views.xml",
        # MENUS
        "views/restaurant_menu_menus.xml",
    ],
}
