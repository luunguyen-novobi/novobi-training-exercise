from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean(default=True)

    def button_archive(self):
        pass