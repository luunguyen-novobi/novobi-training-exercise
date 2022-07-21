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
        'wizard/purchase_order_archives_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}