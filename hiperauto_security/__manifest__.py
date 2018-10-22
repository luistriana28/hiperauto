# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Hiperauto Security',
    'summary': 'Security',
    'version': '10.0.1.0.0',
    'category': 'Uncategorized',
    'website': 'https://odoo-community.org/',
    'author': 'Jarsa Sistemas S.A. de C.V., Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'sale_stock',
        'purchase',
    ],
    'data': ['views/hiperauto_filters.xml',
             'views/hiperauto_security.xml'],
}
