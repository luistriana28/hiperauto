# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import api, fields, models
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
from odoo.exceptions import ValidationError


class GlobalSummaryReportWizard(models.TransientModel):
    _name = 'global.summary.report.wizard'

    date_start = fields.Datetime(
        string='Start Date',
        required=True, default=fields.Datetime.now)
    date_end = fields.Datetime(
        string='End Date', required=True, default=fields.Datetime.now)
    currency_id = fields.Many2one(
        'res.currency', string='Currency',
        default=lambda self: self.env.user.company_id.currency_id)
    
    @api.onchange('date_start')
    def _onchange_date_start(self):
        if self.date_start and self.date_end and self.date_end < self.date_start:
            self.date_end = self.date_start

    @api.onchange('date_end')
    def _onchange_date_end(self):
        if self.date_end and self.date_end < self.date_start:
            self.date_start = self.date_end

    @api.multi
    def print_report(self):
        """
        data
        """
        data = {
            'model': self._name,
            'ids': self.ids,
            'currency_id': self.currency_id,
            'form': {
                'date_start': self.date_start, 
                'date_end': self.date_end
            },
        }
        return self.env.ref('hiperauto_global_report.global_summary_report').report_action(
            self, data=data)


class ReportglobalSummaryReportView(models.AbstractModel):
    """
        Abstract Model specially for report template.
        _name = Use prefix `report.` along with `module_name.report_name`
    """
    _name = 'report.hiperauto_global_report.global_summary_report_view'

    @api.multi
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']

        start_date = datetime.strptime(date_start, DATETIME_FORMAT)
        end_date = datetime.strptime(date_end, DATETIME_FORMAT) - timedelta(hours=5)
        delta = timedelta(days=1)

        docs = []
        total_orders = 0
        total_sales = 0
        total_expense = 0
        taxes = 0
        services = 0
        bank_comission = 0
        ads = 0
        loans = 0
        payroll = 0
        total_purchase = 0

        while start_date <= end_date:
            date = start_date
            start_date += delta

            orders = self.env['sale.order'].search([
                ('date_order', '>=', date.strftime(DATETIME_FORMAT)),
                ('date_order', '<', start_date.strftime(DATETIME_FORMAT)),
                ('state', 'in', ['sale', 'done'])
                ])
            sos = len(orders)
            sales = sum(order.amount_total for order in orders)
            total_orders += sos
            total_sales += sales

            purchases = self.env['account.invoice'].search([
                ('date_invoice', '>=', date.strftime(DATETIME_FORMAT)),
                ('date_invoice', '<', start_date.strftime(DATETIME_FORMAT)),
                ('state', 'in', ['open', 'paid']),
                ('type', '=', 'in_invoice'),
                ('journal_id', 'in', [27, 11, 17, 23, 36])
                ])
            purchase = sum(purc.amount_total for purc in purchases)
            total_purchase += purchase

            invoices = self.env['account.invoice'].search([
                ('date_invoice', '>=', date.strftime(DATETIME_FORMAT)),
                ('date_invoice', '<', start_date.strftime(DATETIME_FORMAT)),
                ('state', 'in', ['open', 'paid']), ('type', '=', 'in_invoice'),
                ('journal_id', 'not in', [27, 11, 17, 23, 36])])
            
            for inv in invoices:
                if inv.partner_id.category_id:
                    if inv.partner_id.category_id.name == 'IMPUESTOS':
                        taxes += inv.amount_total
                    elif inv.partner_id.category_id.name == 'COMISION BANCO':
                        bank_comission += inv.amount_total
                    elif inv.partner_id.category_id.name == 'NOMINA':
                        payroll += inv.amount_total
                    elif inv.partner_id.category_id.name == 'SERVICIOS':
                        services += inv.amount_total
                    elif inv.partner_id.category_id.name == 'PUBLICIDAD':
                        ads += inv.amount_total
                    elif inv.partner_id.category_id.name == 'PRESTAMOS':
                        loans += inv.amount_total
                else: 
                    total_expense += inv.amount_total
        total_expenses = (
            taxes + bank_comission + payroll +
            services + ads + loans + total_expense + total_purchase)
        docs.append({
            'total_orders': total_orders,
            'total_sales': total_sales,
            'taxes': taxes,
            'payroll': payroll,
            'total_purchase': total_purchase,
            'services': services,
            'ads': ads,
            'bank_comission': bank_comission,
            'loans': loans,
            'utility': (total_sales - total_expenses),
            'p_utility': (((total_sales - total_expenses) * 100) / total_sales),
            'p_ref': (((total_sales / total_purchase) * 100) - 100),
            'total_expense': total_expense,
            'prom': (total_sales / total_orders if total_orders != 0 else False),
            'company': self.env.user.company_id,
            'currency_id': self.env.user.company_id.currency_id
        })

        docargs = {
            'date_start': data['form']['date_start'],
            'date_end': data['form']['date_end'],
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'docs': docs,
        }
        return docargs
