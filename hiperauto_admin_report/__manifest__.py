# -*- coding: utf-8 -*-

{
    "name": "Hiperauto Admon Report",
    "category": "Hidden",
    "author": "",
    "summary": "Admon summary report",
    "version": "1.0",
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
