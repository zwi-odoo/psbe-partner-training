from odoo import fields, models


class RestaurantMenu(models.Model):
    _name = "restaurant.menu"
    _description = "Restaurant Menu"

    name = fields.Char(required=True)
    description = fields.Text()

    menu_item_ids = fields.Many2many(
        comodel_name="restaurant.menu.item",
        relation="menu_item_rel",
        column1="menu_id",
        column2="menu_item_id",
    )
