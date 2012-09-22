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
    'name': 'Customer Configuration Parameters Manager',
    'version': '0.1',
    'category': 'Configuration',
    'description': """
    ITA: Consente la gestione dei parametri di configurazione dedicati ai clienti
    ENG: Allow to manage the customer dedicated configuration parameters""",
    'author': 'www.andreacometa.it',
    'website': 'http://www.andreacometa.it',
    'license': 'AGPL-3',
    "active": False,
    "installable": True,
    "depends" : ['base'],
    "update_xml" : ['config_parameter_view.xml'],
    "images" : ['images/image.png'],
}
