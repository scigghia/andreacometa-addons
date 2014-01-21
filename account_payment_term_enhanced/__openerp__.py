# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2012 Andrea Cometa All Rights Reserved.
#                       www.andreacometa.it
#                       openerp@andreacometa.it
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
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
    'name': 'Account Payment Term Enhanced',
    'version': '1.1',
    'category': 'Accounting & Finance',
    'description': """
ITA: Aggiunge la possibilità di calcolare le scadenze ripartendole equamente
     Permette di calcolare le scadenze per mese oltre che per giorni.
ENG: Adds the ability to calculate maturities basing them equally.
     Adds due date calc based on months instead days""",
    'author': 'www.andreacometa.it',
    'website': 'http://www.andreacometa.it',
    'depends': ['account'],
    'update_xml': ['account_view.xml', ],
    'installable': True,
    'active': False,
    'images': ['images/image.png'],
}
