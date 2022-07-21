from odoo import models, fields

class PurchaseOrderArchives(models.TransientModel):
    _name = 'purchase.order.archives.wizard'

    purchase_orders_ids = fields.Many2many('purchase.order', domain=['&', ('active', '=', True), '|', ('state', '=', 'done'), ('state', '=', 'cancel')])

    def action_archive(self):
        self.purchase_orders_ids.action_archive_purchase_orders()
            
        
