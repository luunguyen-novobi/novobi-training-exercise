from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean(default=True)
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
        lifespan = self.env['ir.config_parameter'].get_param('purchase.order.enhancement.settings.lifespan')
        archive_date = datetime.now() - timedelta(days=int(lifespan))
        self.search(['&', ('write_date', '<', archive_date), ('state', 'in', ('done', 'cancel'))]).action_archive_purchase_orders()