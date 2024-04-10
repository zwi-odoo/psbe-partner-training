from odoo import fields, models


class RestaurantMenuItems(models.Model):
    _name = "restaurant.menu.item"
    _description = "Restaurant Menu Item"

    name = fields.Char(required=True)
    description = fields.Text()

    price = fields.Float(required=True)
    category = fields.Selection(
        selection=[
            ("appetizer", "Appetizer"),
            ("main", "Main Course"),
            ("dessert", "Dessert"),
        ],
        required=True,
    )
    is_available = fields.Boolean(default=True)
