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
    'name': 'Account tax required',
    'version': '0.1',
    'category': 'Finance',
    'description': """
    ITA: Rende obbligatoria almeno un'aliquota iva nelle righe di fattura
    ENG: Makes mandatory at least one tax rate in the invoice lines
    """,
    'author': 'www.andreacometa.it',
    'website': 'http://www.andreacometa.it',
    'license': 'AGPL-3',
    "active": False,
    "installable": True,
    "depends" : ['account', 'account_invoice_layout'],
    "update_xml" : ['account/account_view.xml',],
    "images" : ['images/image.png'],
}
