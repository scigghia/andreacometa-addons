# -*- encoding: utf-8 -*-
##############################################################################
#
#    Personalizzazione realizzata da Francesco OpenCode Apruzzese (f.apruzzese@andreacometa.it)
#    Compatible with OpenERP release 6.1.X
#    Copyright (C) 2012 Andrea Cometa. All Rights Reserved.
#    Email: cescoap@gmail.com, info@andreacometa.it
#    Web site: http://www.andreacometa.it
#
##############################################################################

{
    'name': 'Customer Configuration Parameters Manager',
    'version': '0.1',
    'category': 'Configuration',
    'description': """
    ITA: Modulo per la gestione dei parametri di configurazione dedicati ai clienti
    ENG: Module to managing the customer dedicated configuration parameters""",
    'author': 'Apruzzese Francesco',
    'website': 'http://www.andreacometa.it',
    'license': 'AGPL-3',
    "active": False,
    "installable": True,
    "depends" : ['base'],
    "update_xml" : ['config_parameter_view.xml'],
}
