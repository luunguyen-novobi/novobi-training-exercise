from odoo import models, fields

class PurchaseOrderSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    lifespan = fields.Integer(default=0)

    def set_values(self):
        super(PurchaseOrderSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('purchase.order.enhancement.settings.lifespan', self.lifespan)

    def get_values(self):
        res = super(PurchaseOrderSettings, self).get_values()
        lifespan = self.env['ir.config_parameter'].get_param('purchase.order.enhancement.settings.lifespan')
        res.update({'lifespan': lifespan})
        return res