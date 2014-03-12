# -*- encoding: utf-8 -*-
from osv import osv, fields

class sale_shop(osv.osv):
    _name = 'sale.shop'
    _inherit = 'sale.shop'
    _columns = {
                'shop_user_id':fields.many2many('res.users', 'res_users_rel', 'shop_id', 'users_id', 'Responsables'),
        }
sale_shop()