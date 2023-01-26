# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields


class SaleOrderStage(models.Model):
    _name = 'sale.order.stage'
    _description = 'Stages of Sale orders'
    _order = 'sequence'

    name = fields.Char(
        string='Description', translate=True, required=True)
    active = fields.Boolean(
        string='Active', default=True)
    sequence = fields.Integer(
        strng='Sequence')
