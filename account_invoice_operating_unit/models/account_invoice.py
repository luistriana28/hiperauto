# -*- coding: utf-8 -*-
# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.model
    def default_get(self, fields):
        res = super(AccountInvoice, self).default_get(fields)
        if self._context.get('default_journal_id'):
            return res
        active_model = self._context.get('active_model')
        user_ou = self.env.user.operating_unit_ids
        if active_model == 'sale.order' and res.get('journal_id'):
            active_journal = self.env['account.journal'].browse(
                res['journal_id'])
            if not active_journal.operating_unit_id:
                return res
            elif active_journal.operating_unit_id in user_ou:
                return res
        journal_type = (
            'sale' if res.get('type') in ['out_invoice', 'out_refund'] or
            active_model == 'sale.order' else 'purchase')
        journal_id = self.env['account.journal'].search([(
            'type', '=', journal_type),
            ('operating_unit_id', 'in', user_ou.ids)], limit=1)
        res['journal_id'] = self.with_context(
            default_journal_id=journal_id.id)._default_journal().id
        return res
