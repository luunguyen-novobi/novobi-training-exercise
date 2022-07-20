from odoo import models, fields
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean(default=True)

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
                