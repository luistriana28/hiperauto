# -*- encoding: utf-8 -*-
from odoo import fields, models
from datetime import datetime


class fleet_vehicle_year(models.Model):
    _inherit = 'fleet.vehicle'

    years = [(num, str(num)) for num in range(1970, (datetime.now().year)+1)]

    year = fields.Selection(years, 'Year')
    driver_id_custom = fields.Many2one(
        'res.partner', 'Customer', domain="[('customer','=',True)]",
        required=True,)
    vin_sn_custom = fields.Char(string='No Serie', size=40,)
