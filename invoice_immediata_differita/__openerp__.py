# -*- encoding: utf-8 -*-
##############################################################################
#
#    Personalizzazione realizzata da Francesco OpenCode Apruzzese (f.apruzzese@andreacometa.it)
#    Compatible with OpenERP release 6.1.X
#    Copyright (C) 2012 Andrea Cometa. All Rights Reserved.
#    Email: cescoap@gmail.com, info@andreacometa.it
#    Web site: http://www.andreacometa.it
#
##########################################################################

{
    'name': 'Invoice Immediata-Differita',
    'version': '0.1',
    'category': 'Finance',
    'description': """
    ITA : Modulo per la separazione tra fatture immediate e differite (Utile come base per moduli più complessi)
          Impostare in ir_config_parameter due valori con chiavi 'report_invoice_immediate' e 'report_invoice_differate' e come
          valori i nomi dei report da richiamare in fase di stampa
    ENG: Module for the separation of immediate and deferred invoices (Useful as a basis for more complex modules)
          Set in ir_config_parameter two values ​​with keys 'report_invoice_immediate' and 'report_invoice_differate' and how
          values ​​the names of reports to call for print
    """,
    'author': 'www.andreacometa.it',
    'website': 'http://www.andreacometa.it',
    'license': 'AGPL-3',
    "active": False,
    "installable": True,
    "depends" : ['account',],
    "update_xml" : ['account/account_view.xml',],
}
