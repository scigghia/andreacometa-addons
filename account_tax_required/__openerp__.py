# -*- encoding: utf-8 -*-
##############################################################################
#
#    Modulo realizzato da Apruzzese Francesco
#    Compatible with OpenERP release 6.0.0
#    Copyright (C) 2010 Andrea Cometa. All Rights Reserved.
#    Email: cescoap@gmail.com
#    Web site: http://www.andreacometa.it
#
##############################################################################

{
    'name': 'Account tax required',
    'version': '0.1',
    'category': 'Finance',
    'description': """
    ITA : Modulo per rendere obbligatoria almeno un'aliquota iva nelle righe di fattura
    ENG: Module to make required at least a rate of VAT in the invoice lines
    """,
    'author': 'www.andreacometa.it',
    'website': 'http://www.andreacometa.it',
    'license': 'AGPL-3',
    "active": False,
    "installable": True,
    "depends" : ['account', 'account_invoice_layout'],
    "update_xml" : ['account/account_view.xml',],
}
