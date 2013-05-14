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

from osv import fields, osv


class account_invoice_line(osv.osv):

	_name = "account.invoice.line"
	_inherit = "account.invoice.line"

	_columns = {
		'sconto_primario' : fields.float('Sconto (%)'),
		'sconto_aggiuntivo' : fields.float('Sconto 2 (%)'),
	}

	# ----- Genera lo sconto globale tenendo presente i due sconti inseriti
	def onchange_sconti(self, cr, uid, ids, sconto_primario, sconto_secondario):
		res = {}
		res['discount'] = 100 - ((100.00-sconto_primario) * (100.00-sconto_secondario) / 100)
		return {'value':res}

account_invoice_line()
