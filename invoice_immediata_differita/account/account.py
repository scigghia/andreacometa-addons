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
from tools.translate import _

class account_invoice(osv.osv):

	_name = "account.invoice"
	_inherit = "account.invoice"

	def print_imm_diff_invoice(self, cr, uid, ids, context=None):
		ir_values_obj = self.pool.get('ir.config_parameter')
		if self.browse(cr, uid, ids, context)[0].immediate:
			report_name = ir_values_obj.get_param(cr, uid, 'report_invoice_immediate', False)
		else:
			report_name = ir_values_obj.get_param(cr, uid, 'report_invoice_differita', False)
		if not report_name:
			raise osv.except_osv(_('Attenzione'), _('Impostare un report di stampa'))
			return False
		return {
			'type':'ir.actions.report.xml',
			'report_name': report_name,
			'datas': {
				'model':'account.invoice',
				'ids': ids,
				'report_type': 'pdf',
			},
			'nodestroy': True,
		}

	_columns = {
		'immediate' : fields.boolean('Fattura Immediata'),
	}
	
	_defaults = {
		'immediate' : False,
	}

account_invoice()
