# -*- coding: utf-8 -*-
{
    'name': "[DELTAPURO] SO REPORT",

    'summary': """
        Template baru SO modifikasi
    """,

    'description': """
        Features
	======================================================================
	* Dapat menampilkan gambar dalam report
    """,

    'author': "OSYS [RIZAL]",
    'website': "https://www.osys.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/so.xml',
        'reports/proforma_invoice.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
