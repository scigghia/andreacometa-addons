# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2012 Andrea Cometa All Rights Reserved.
#                       www.andreacometa.it
#                       openerp@andreacometa.it
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Invoice Immediata-Differita',
    'version': '0.1',
    'category': 'Finance',
    'description': """
    ITA : Modulo per la separazione tra fatture immediate e differite (Utile come base per moduli più complessi)
          Impostare in ir_config_parameter due valori con chiavi 'report_invoice_immediate' e 'report_invoice_differite' e come
          valori i nomi dei report da richiamare in fase di stampa
    ENG: Module for the separation of immediate and deferred invoices (Useful as a basis for more complex modules)
          Set in ir_config_parameter two values ​​with keys 'report_invoice_immediate' and 'report_invoice_diffirate' and how
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
