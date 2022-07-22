from odoo import models, fields

class PurchaseOrderSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    lifespan = fields.Integer(default=0, config_parameter='purchase.order.enhancement.settings.lifespan')