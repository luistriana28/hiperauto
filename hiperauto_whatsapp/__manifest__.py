# -*- coding: utf-8 -*-
# Copyright 2021, Luis Triana
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    'name': 'Hiperauto Whatsapp Website',
    'summary': 'Whatsapp Button in Website',
    'version': '12.0.1.0.0',
    'category': 'Website',
    'website': 'https://odoo-community.org/',
    'author': 'Luis Triana, Odoo Community Association (OCA)',
    'license': 'LGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'base',
        'web',
        'website'
    ],
    'data': [
        'views/res_config_settings.xml',
        'views/assets.xml',
        'views/view_website_whatsapp.xml',
    ],
}
