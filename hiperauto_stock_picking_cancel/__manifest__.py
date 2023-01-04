# Copyright 2023
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Hiperauto Stock Picking Cancel',
    'summary': 'Cancel Incoming and Outgoing Shipment/picking',
    'version': '12.0.1.0.0',
    'category': 'Stock',
    'website': 'https://odoo-community.org/',
    'author': 'Odoo Community Association (OCA)',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'depends': [
        'base',
        'stock'
    ],
    'data': [
        'views/inherited_stock_picking.xml',
    ]
}
