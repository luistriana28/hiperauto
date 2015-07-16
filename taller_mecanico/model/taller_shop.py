# -*- encoding: utf-8 -*-
from osv import osv, fields


class sale_shop(osv.osv):
    _name = 'sale.shop'
    _inherit = 'sale.shop'
    _columns = {
        'shop_user_id': fields.many2many('res.users',
                                         'res_users_rel',
                                         'shop_id',
                                         'users_id',
                                         'Responsables'),
        }


class account_journal(osv.osv):
    _name = 'account.journal'
    _inherit = 'account.journal'
    _columns = {
        'journal_user_id': fields.many2many('res.users',
                                            'res_users1_rel',
                                            'journal_id',
                                            'users_id',
                                            'Responsables'),
        }


class stock_warehouse(osv.osv):
    _name = 'stock.warehouse'
    _inherit = 'stock.warehouse'
    _columns = {
        'warehouse_user_id': fields.many2many('res.users',
                                              'res_users2_rel',
                                              'ware',
                                              'users_id',
                                              'Responsables'),
        }
