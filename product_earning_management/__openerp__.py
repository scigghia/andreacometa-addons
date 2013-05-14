# -*- encoding: utf-8 -*-
##############################################################################
#
#    Personalizzazione realizzata da Francesco OpenCode Apruzzese (f.apruzzese@andreacometa.it)
#    Compatible with OpenERP release 6.1.X
#    Copyright (C) 2010 Andrea Cometa. All Rights Reserved.
#    Email: info@andreacometa.it, f.apruzzese@andreacometa.it
#    Web site: http://www.andreacometa.it
#
##############################################################################

{
    'name': "product_earning_management",
    'version': '0.1',
    'category': 'Product',
    'description': """
    ITA: Permette di gestire il guadagno percentuale che si ha su un prodotto
    ENG: It's possibile to manage the earning on the products prices""",
    'author': 'www.andreacometa.it',
    'website': 'http://www.andreacometa.it',
    'license': 'AGPL-3',
    "depends" : ['product', 'stock'],
    "init_xml" : [],
    "update_xml" : [
        'product/product_view.xml',
        ],
    "demo_xml" : [],
    "active": False,
    "installable": True,
    "images" : [],
}
