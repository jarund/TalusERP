# -*- coding: utf-8 -*-
{
    'name': "talus_helpdesk_updates",

    'summary': """
        Helpdesk Updates""",

    'description': """
        Helpdesk updates, changing description to html, adding Internal notes tab in html format.
    """,

    'author': "Talus ERP",
    'website': "http://www.taluserp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk', 'hr_timesheet'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
