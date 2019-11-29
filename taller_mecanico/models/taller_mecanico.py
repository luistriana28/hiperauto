from odoo import fields, models


class sale_order(models.Model):
    _inherit = 'sale.order'

    vehicle_id = fields.Many2one(
        'fleet.vehicle',
        domain="['|',('driver_id_custom','=',partner_id),"
        "('driver_id_custom','=',False)]",
        string="Vehicle", required=True,)
