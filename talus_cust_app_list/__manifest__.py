# -*- coding: utf-8 -*-
{
    'name': "talus_cust_app_list",

    'summary': """
        Hold a list of app installed per Customer""",

    'description': """
        Hold a list of Modules installed per Customer and DB Code added per customer.  Useful for upgrading.
    """,

    'author': "Talus ERP",
    'website': "http://www.taluserp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
