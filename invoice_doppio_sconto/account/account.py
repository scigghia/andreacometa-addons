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
