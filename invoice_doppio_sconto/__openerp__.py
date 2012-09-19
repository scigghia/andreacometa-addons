# -*- encoding: utf-8 -*-
##############################################################################
#
#    Modulo realizzato da Francesco OpenCode Apruzzese (f.apruzzese@andreacometa.it)
#    Compatible with OpenERP release 6.1.X
#    Copyright (C) 2012 Andrea Cometa. All Rights Reserved.
#    Email: info@andreacometa.it, f.apruzzese@andreacometa.it
#    Web site: http://www.andreacometa.it
#
##########################################################################

{
    'name': 'Doppio Sconto in fattura - Invoices with two discounts',
    'version': '0.1',
    'category': 'Finance',
    'description': """
    ITA : Modulo per gestire due sconti all\'interno della fatturazione
    ENG: Module to manage invoices with two discounts
    """,
    'author': 'www.andreacometa.it',
    'website': 'http://www.andreacometa.it',
    'license': 'AGPL-3',
    "active": False,
    "installable": True,
    "depends" : ['account',],
    "update_xml" : ['account/account_view.xml',],
    'images' : ['images/image.png'],
}
