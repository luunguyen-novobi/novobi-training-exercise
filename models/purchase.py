from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    active = fields.Boolean(default=True)
    partner_phone = fields.Char(string="Vendor Phone", store=False, compute='_compute_partner_phone', inverse='_inverse_partner_phone')

    def _compute_partner_phone(self):
        for record in self:
            record.partner_phone = record.partner_id.phone

    def _inverse_partner_phone(self):
        for record in self:
            record.partner_id.phone = record.partner_phone

    def action_archive_purchase_orders(self, from_api=False):
        if not from_api and not self.env.user.has_group('purchase.group_purchase_manager'):
            raise AccessError('You don\'t have the access rights')

        not_archive_orders = self.filtered(lambda record: record.state not in ('done', 'cancel'))
        if len(not_archive_orders) > 0:
            raise UserError('Only allow archive the locked or canceled purchase orders')

        self.write({'active': False})

    def action_unarchive_purchase_orders(self):
        self.write({'active': True})

    @api.model
    def _cron_archive_po(self):
        lifespan = self.env['ir.config_parameter'].get_param('purchase.order.enhancement.settings.lifespan')
        archive_date = datetime.now() - timedelta(days=int(lifespan))
        self.search(['&', ('write_date', '<', archive_date), ('state', 'in', ('done', 'cancel'))]).action_archive_purchase_orders()