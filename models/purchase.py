from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean(default=True)
    lifespan = fields.Integer(default=0)
    usphone = fields.Char(string="Phone (US Format)")

    def action_archive_purchase_orders(self):
        for record in self:
            if record.state == 'done' or record.state == 'cancel':
                record.active = False
            else:
                raise UserError('Only allow archive the locked or canceled purchase orders')
    
    def action_unarchive_purchase_orders(self):
        for record in self:
            if record.state == 'done' or record.state == 'cancel':
                record.active = True
            else:
                raise UserError('Only allow unarchive the locked or canceled purchase orders')

    @api.model
    def _cron_archive_po(self):
        self.search([('state', 'in', ('done', 'cancel'))]).filtered(lambda record: datetime.now() > record.write_date + timedelta(record.lifespan)).action_archive_purchase_orders()