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

from osv import fields, osv


class account_invoice(osv.osv):

	_name = "account.invoice"
	_inherit = "account.invoice"

	def print_imm_diff_invoice(self, cr, uid, ids, context=None):
		ir_values_obj = self.pool.get('ir.config_parameter')
		if self.browse(cr, uid, ids, context)[0].immediate:
			report_name = ir_values_obj.get_param(cr, uid, 'report_invoice_immediate', False)
		else:
			report_name = ir_values_obj.get_param(cr, uid, 'report_invoice_differate', False)
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
		'immediate' : fields.boolean('Immediate'),
	}
	
	_defaults = {
		'immediate' : False,
	}

account_invoice()
