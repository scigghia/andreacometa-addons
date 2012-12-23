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
	'name': 'Modulo per la gestione del recupero dei buchi dei protocolli fiscali',
	'version': '1.0',
	'category': 'Custom',
	'description': 
		"""
		Modulo per la gestione del recupero dei buchi delle sequence (DDT, Fatture, etc.)
		Basta ereditare l'unlink di una classe con sequence per ottenere la funzionalità di ripristino
		""",
	'author': 'www.andreacometa.it',
	'website': 'http://www.andreacometa.it',
	'license': 'AGPL-3',
	"active": False,
	"installable": True,
	"depends" : ['base','account','stock',],
	"update_xml" : [
		'base/sequence_view.xml',
		'security/recupero_protocolli_security.xml',
		'security/ir.model.access.csv',
		],
}
