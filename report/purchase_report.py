from odoo import models, fields

class PurchaseOrderReport(models.Model):
    _inherit = 'purchase.report'

    payment_term_id = fields.Many2one('account.payment.term', 'Payment Terms', domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")