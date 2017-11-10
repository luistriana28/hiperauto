# -*- encoding: utf-8 -*-
from odoo import fields, models


class sale_order(models.Model):
    _inherit = 'sale.order'
    
    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle", required=True,)
