#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017, Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Invoice Report for Hiperauto",
    "version": "12.0.0.1.0",
    "category": "Report",
    "author": "Jarsa Sistemas",
    "depends": [
        'account',
        'sale',
        'l10n_mx_edi'
    ],
    "data": [
        'report/l10n_mx_base_report.xml',
    ],
    "installable": True,
}
