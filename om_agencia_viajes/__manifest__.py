# -*- coding: utf-8 -*-
{
    'name': "Administración de Agencia de Viajes",

    'summary': """
        Administra viajes y viajeros
    """,

    'description': """
        Simple ejemplo de un modulo personalizado
    """,

    'author': "Agencia de Viajes",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',
    'installable': True,
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/viajes.xml',
        'views/viajeros.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
