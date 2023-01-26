# Copyright 2022 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Sale Order Stage",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/odoo-addons",
    "category": "Sales",
    "depends": [
        "sale_management",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_stage_views.xml",
        "views/sale_order_views.xml",
    ],
    "installable": True,
}
