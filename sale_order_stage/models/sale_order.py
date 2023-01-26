# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    stage_id = fields.Many2one(
        string='Stage', comodel_name='sale.order.stage')
