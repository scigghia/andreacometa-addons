# -*- coding: utf-8 -*-
##############################################################################
#    
#    Modulo realizzato da Andrea Cometa (info@andreacometa.it)
#    Compatible with OpenERP release 6.1.X
#    Copyright (C) 2012 Andrea Cometa. All Rights Reserved.
#    Email: info@andreacometa.it
#    Web site: http://www.andreacometa.it
#
##############################################################################
{
    'name': "Payments Due list Exdended",
    'version': '0.1',
    'category': 'Generic Modules/Payment',
    'description': """ENG:Original Domsense model extended\nITA:Rappresenta un vero e proprio scadenzario""",
    'author': 'www.andreacometa.it',
    'website': 'http://www.andreacometa.it',
    'license': 'AGPL-3',
    "depends" : ['account_due_list', 'report_webkit'],
    "init_xml" : [],
    "update_xml" : [
        'account/account_view.xml',
        'reports/reports.xml',
        'payment_type_data.xml',
        ],
    "demo_xml" : [],
    "active": False,
    "installable": True,
    "images": ['images/image.png'],
}
