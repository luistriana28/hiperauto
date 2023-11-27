# -*- coding: utf-8 -*-

{
    "name": "Hiperauto Global Admon Report",
    "category": "Hidden",
    "author": "",
    "summary": "Global Admon summary report",
    "version": "12.0.1.0.0",
    "description": """
        Sample custom report for Hiperauto Admon
    """,
    "depends": [
        "sale_management"
    ],
    "data": [
        'data/data.xml',
        'report/admon_summary.xml',
        'wizard/admon_order_summary_wizard.xml',
    ],
    "installable": True,
}
