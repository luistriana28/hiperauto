# Copyright 2023, Luis Triana
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Hiperauto New Client Bool',
    'summary': 'Hiperauto New Client Bool',
    'version': '12.0.1.0.0',
    'category': 'sale',
    'website': 'https://odoo-community.org/',
    'author': 'Luis Triana, Odoo Community Association (OCA)',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'sale',
    ],
    'data': [
        'views/sale_order_view.xml',
    ]
}