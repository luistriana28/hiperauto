# Copyright 2018, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Hiperauto Instance',
    'summary': 'Instance for Hiperauto',
    'version': '10.0.1.0.0',
    'category': 'Base',
    'author': 'Jarsa Sistemas',
    'website': 'https://www.jarsa.com.mx',
    'license': 'AGPL-3',
    'depends': [
        'hiperauto_security',
        'invoice_custom_report',
        'sale_make_invoice_with_journal',
        'taller_mecanico',
        'hiperauto_custom_views',
    ],
    'installable': True,
}
