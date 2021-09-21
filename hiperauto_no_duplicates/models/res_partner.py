"""
File for Partner
"""

from odoo import models


class ProductProductExt(models.Model):
    _inherit = 'res.partner'

    def clear_duplicates(self):
        """
        Function checking partner
        """
        unique_partner = []  # list of set
        duplicate_partners = []
        is_first = True
        for partner in self:
            temp_unique_partners = unique_partner.copy()
            if not unique_partner:
                unique_partner.append((partner.id, partner.name, partner.vat))
            if not is_first:
                for uni_pro in temp_unique_partners:
                    if partner.name == uni_pro[1]:
                        duplicate_partners.append(partner.id)
                    else:
                        unique_partner.append((partner.id, partner.name, partner.vat))
            is_first = False
        self.browse(list(dict.fromkeys(duplicate_partners))).unlink()
