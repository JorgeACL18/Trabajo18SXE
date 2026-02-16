# -*- coding: utf-8 -*-
{
    'name': "Hospital",
    'summary': "Hospital 100% funcional. Para nada una estafa",
    'description': """
Long description of module's purpose
    """,
    'author': "Jorge",

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/hospital_views.xml',
    ],

    'demo': [
        'demo/hospital_demo.xml',
    ],

    'installable': True,
    'application': True,
}

