from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    visit_count = fields.Integer(
        string="Visit Count", compute="_compute_visit_count")
    is_first_time_customer = fields.Boolean(
        string="First Time Customer", compute="_compute_first_time_customer")

    @api.depends('partner_id')
    def _compute_visit_count(self):
        for order in self:
            order.visit_count = self.env['sale.order'].search_count([('partner_id', '=', order.partner_id.id)])

    @api.depends('visit_count')
    def _compute_first_time_customer(self):
        for order in self:
            order.is_first_time_customer = True if order.visit_count <= 1 else False