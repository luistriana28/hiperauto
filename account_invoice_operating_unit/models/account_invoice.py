# -*- coding: utf-8 -*-
# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    @api.constrains('operating_unit_id', 'journal_id')
    def _check_journal_operating_unit(self):
        for ai in self:
            if (
                ai.journal_id.operating_unit_id and
                ai.operating_unit_id and
                ai.operating_unit_id != ai.journal_id.operating_unit_id
            ):
                if not self.env.user.default_operating_unit_id:
                    return True
                    raise ValidationError(_('The OU in the Invoice and in '
                                            'Journal must be the same.'))
        return True


class SaleOrder(models.Model):
    _inherit= 'sale.order'

    @api.multi
    def _prepare_invoice(self):
        res= super(SaleOrder, self)._prepare_invoice()
        if self.operating_unit_id:
            journal = self.env['account.journal'].search(
                [('operating_unit_id', '=', self.operating_unit_id.id),
                 ('type', '=', 'sale')])
            if journal:
                res.update({'journal_id': journal.id})
        return res

