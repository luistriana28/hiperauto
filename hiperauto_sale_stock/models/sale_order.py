from odoo import _, api, models
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        """
        Super for Sale Order action confirm
        """
        for sale_order in self:
            for sale_order_line in sale_order.order_line:
                if sale_order_line.product_id.type in ['product']:
                    product = sale_order_line.product_id
                    available_qty = product.qty_available
                    sale_qty = sale_order_line.product_uom_qty
                    if not available_qty < sale_qty:
                        continue
                    raise ValidationError(_(
                        'You cannot confirm order without stock. ' +
                        'Product: ' + product.default_code +
                        ' Stock: ' + str(available_qty)))
        return super(SaleOrder, self).action_confirm()
