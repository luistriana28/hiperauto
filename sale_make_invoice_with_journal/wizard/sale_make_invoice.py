# -*- coding: utf-8 -*-
# © 2017 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    journal = fields.Many2one(
        'account.journal',
        domain=lambda self: [
            ('type', '=', 'sale'), '|',
            ('operating_unit_id', 'in', self.env.user.operating_unit_ids.ids),
            ('operating_unit_id', '=', False)])

    @api.model
    def default_get(self):
        res = super(SaleAdvancePaymentInv, self).default_get(fields)
        journals = self.env['account.journal'].search([
            ('type', '=', 'sale'),
            ('operating_unit_id', 'in', self.env.user.operating_unit_ids.ids)
        ], limit=1)
        res['journal'] = journals.id
        return res

    @api.multi
    def create_invoices(self):
        return super(
            SaleAdvancePaymentInv,
            self.with_context(default_journal_id=self.journal.id)
        ).create_invoices()
