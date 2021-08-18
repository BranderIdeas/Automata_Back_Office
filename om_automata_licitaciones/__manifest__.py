# -*- coding: utf-8 -*-
{
    'name': "Licitaciones",

    'summary': """
        Personalización para CRM""",

    'description': """
        Personalización para CRM
    """,

    'author': "Automata & Brander Ideas SAS",
    'website': "https://www.branderideas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'crm',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/crm_lead_view_form_inherit.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
