# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('authorized', 'Authorized'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', track_sequence=3, default='draft')

    @api.multi
    def action_authorized(self):
        return self.write({'state': 'authorized'})