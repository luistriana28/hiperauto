# © 2017 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Sale make invoice with journal',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'website': 'comunitea.com',
    'author': 'Comunitea',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'sale_operating_unit',
    ],
    'data': [
        'wizard/sale_make_invoice.xml'
    ],
}
