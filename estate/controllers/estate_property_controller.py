# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

import json


class EstatePropertyController(http.Controller):

    @http.route('/estate/property/new', type='json', auth='public', methods=['POST'])
    def post_new_property(self, **kwargs):
        payload = json.loads(request.httprequest.data)

        # seller
        Partner = request.env['res.partner'].sudo()
        seller_email = payload.get('seller_email')
        seller = Partner.search([
            ('email', '=', seller_email)
        ])
        if not seller:
            vals = {
                'name': payload.get('seller_name'),
                'email': seller_email
            }
            seller = Partner.create(vals)

        # type
        PropertyType = request.env['estate.property.type'].sudo()
        property_type = PropertyType.search([
            ('code', '=', payload.get('type'))
        ])

        # property
        Property = request.env['estate.property'].sudo()
        vals = {
            'name': payload.get('name'),
            'description': payload.get('description'),
            'expected_price': payload.get('price'),
            'seller_id': seller.id,
            'property_type_id': property_type.id,
        }
        property = Property.create(vals)
        return {'property_id': property.id}
