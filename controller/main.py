from odoo import http
from odoo.http import request

class PurchaseOrderEnhancementRoute(http.Controller):
    
    @http.route('/purchase/order/archives', type='json', methods=['POST'], auth='none', csrf=False)
    def archive_multiple_purchase_orders(self, **kwargs):
        method, purchase_order_ids = kwargs.get('method'), kwargs.get('orders')
        result = {"archived_orders": False, "code": 404, "message": "Could not found"}
        if method != 'archive':
            return result
        else:
            purchase_orders = request.env['purchase.order'].sudo().browse(purchase_order_ids)
            try:
                purchase_orders.action_archive_purchase_orders()
                result['archived_orders'] = purchase_order_ids
                result['code'] = 200
                result['message'] = 'Successful'
                return result
            except Exception as e:
                result['message'] = str(e)
                return result