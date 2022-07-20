{
    'name': 'Purchase Order Enhancement',
    'version': '1.0',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order_enhancement.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}