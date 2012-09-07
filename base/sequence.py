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


class ir_protocolli_da_recuperare(osv.osv):

	_name = "ir.protocolli_da_recuperare"
	_description = "ir.protocolli_da_recuperare"

	_columns = {
		'name' : fields.char('Classe',size=32),
		'sequence_id' : fields.many2one('ir.sequence', 'Sequence'),
		'protocollo' : fields.char('Protocollo', size=32),
		'data' : fields.date('Data'),
	}

	_order = "protocollo asc"

ir_protocolli_da_recuperare()


class ir_sequence(osv.osv):
	_name = "ir.sequence"
	_inherit = "ir.sequence"


	def next_by_id(self, cr, uid, sequence_id, context=None):
		recuperare_obj = self.pool.get('ir.protocolli_da_recuperare')
		recuperare_ids = recuperare_obj.search(cr, uid, [('sequence_id', '=', sequence_id)])
		if recuperare_ids:
			# ----- Se lo trova ne recupera il protocollo e lo cancella
			recuperare_id = recuperare_ids[0]
			protocollo = recuperare_obj.browse(cr, uid, recuperare_id).protocollo
			recuperare_obj.unlink(cr, uid, recuperare_id)
			return protocollo
		else:
			return super(ir_sequence, self).next_by_id(cr, uid, sequence_id, context)

	def next_by_code(self, cr, uid, sequence_code, context=None):
		recuperare_obj = self.pool.get('ir.protocolli_da_recuperare')
		recuperare_ids = recuperare_obj.search(cr, uid, [('name', '=', sequence_code)])
		if recuperare_ids:
			# ----- Se lo trova ne recupera il protocollo e lo cancella
			recuperare_id = recuperare_ids[0]
			protocollo = recuperare_obj.browse(cr, uid, recuperare_id).protocollo
			recuperare_obj.unlink(cr, uid, recuperare_id)
			return protocollo
		else:
			return super(ir_sequence, self).next_by_code(cr, uid, sequence_code, context)

ir_sequence()
