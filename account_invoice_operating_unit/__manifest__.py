# -*- coding: utf-8 -*-
# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Invoice Operating Unit',
    'version': '12.0.1.0.0',
    'category': 'Account',
    'author': 'Jarsa Sistemas',
    'description': 'Write journal_id corresponding',
    'summary': 'Set the default journal to the invoices',
    'license': 'AGPL-3',
    'depends': [
        'operating_unit',
        'account_operating_unit',
        'sale'
    ],
    'installable': True,
}
