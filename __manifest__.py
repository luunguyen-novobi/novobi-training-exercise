{
    'name': 'Purchase Order Enhancement',
    'version': '1.0',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'purchase'
    ],
    'data': [
        'data/ir_cron_archive_po.xml',
        'report/purchase_order_pdf.xml',
        'report/purchase_order_analysis_pivot.xml',
        'security/ir.model.access.csv',
        'views/purchase_order_enhancement.xml',
        'views/purchase_order_enhancement_settings.xml',
        'wizard/purchase_order_archives_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'purchase_order_enhancement/static/src/js/us_phone.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False
}