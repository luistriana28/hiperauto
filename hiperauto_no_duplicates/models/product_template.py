# -*- coding: utf-8 -*-
##############################################################################
# Module for Check and Delete Duplicate Products (product.templates)
##############################################################################

from odoo import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    """
    Function checking saved info
    """

    def clear_duplicates(self):
        unique_product = []  # list of set
        duplicate_products = []
        is_first = True
        for product in self:
            temp_unique_partners = unique_product.copy()
            if not unique_product:
                unique_product.append((product.id, product.default_code, product.name))
            if not is_first:
                for uni_pro in temp_unique_partners:
                    if product.default_code == uni_pro[1] or product.name == uni_pro[2]:
                        duplicate_products.append(product.id)
                    else:
                        unique_product.append((product.id, product.default_code, product.name))
            is_first = False
        self.browse(list(dict.fromkeys(duplicate_products))).unlink()
