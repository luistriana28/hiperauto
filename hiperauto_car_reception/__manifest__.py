# Copyright 2021, LUIS TRIANA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Hiperauto Car Reception',
    'summary': 'Module summary',
    'version': '12.0.1.0.0',
    'category': 'Uncategorized',
    'website': 'https://odoo-community.org/',
    'author': 'Luis Triana, Odoo Community Association (OCA)',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'depends': [
        'base',
        'sale'
    ],
    'data': [
        'view/some_model_view.xml',
    ]
}