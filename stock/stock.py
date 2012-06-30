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


class stock_picking(osv.osv):

	_name = "stock.picking"
	_inherit = "stock.picking"

	def unlink(self, cr, uid, ids, context=None):
		# ----- Cicla gli indici per scrivere nella tabella di recupero protocolli
		for stock_id in ids:
			protocollo = self.browse(cr, uid, stock_id).ddt_number
			if protocollo:
				data = self.browse(cr, uid, stock_id).date
				self.pool.get('ir.protocolli_da_recuperare').create(cr, uid,
					{'name':'stock.ddt', 'protocollo':protocollo, 'data':data})
		return super(stock_picking, self).unlink(cr, uid, ids, context=None)

stock_picking()
