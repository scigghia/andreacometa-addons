# -*- encoding: utf-8 -*-
##############################################################################
#
#    Personalizzazione realizzata da Francesco OpenCode Apruzzese
#    Compatible with OpenERP release 6.0.0
#    Copyright (C) 2010 Andrea Cometa. All Rights Reserved.
#    Email: info@andreacometa.it
#    Web site: http://www.andreacometa.it
#
##############################################################################

from osv import fields, osv


class account_invoice(osv.osv):

	_name = "account.invoice"
	_inherit = "account.invoice"

	def unlink(self, cr, uid, ids, context=None):
		# ----- Cicla gli indici per scrivere nella tabella di recupero protocolli
		for account_id in ids:
			protocollo_obj = self.browse(cr, uid, account_id)
			protocollo = protocollo_obj.internal_number
			sequence_id = protocollo_obj.journal_id.sequence_id.id
			if protocollo:
				data = self.browse(cr, uid, account_id).date_invoice
				self.pool.get('ir.protocolli_da_recuperare').create(cr, uid,
					{'name':'account.journal', 
					'protocollo':protocollo,
					'data':data,
					'sequence_id' : sequence_id, })
		return super(account_invoice, self).unlink(cr, uid, ids, context=None)

account_invoice()
