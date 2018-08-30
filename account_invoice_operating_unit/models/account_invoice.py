# -*- coding: utf-8 -*-
# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.model
    def default_get(self, fields):
        res = super(AccountInvoice, self).default_get(fields)
        active_model = self._context.get('active_model')
        journal_type = (
            'sale' if res.get('type') in ['out_invoice', 'out_refund'] or
            active_model == 'sale.order' else 'purchase')
        journal_id = self.env['account.journal'].search([(
            'type', '=', journal_type),
            ('operating_unit_id', 'in',
                self.env.user.operating_unit_ids.ids)], limit=1)
        res['journal_id'] = self.with_context(
            default_journal_id=journal_id.id)._default_journal().id
        return res
