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



	#def get(self, cr, uid, code):
	def get_id(self, cr, uid, code, test='id', context=None):
		# ----- Cerca eventuali protocolli da recuperare
		recuperare_obj = self.pool.get('ir.protocolli_da_recuperare')
		if test == 'code':
			recuperare_ids = recuperare_obj.search(cr, uid, [('name', '=', code)])
		else:
			recuperare_ids = recuperare_obj.search(cr, uid, [('sequence_id', '=', code)])
		if recuperare_ids:
			# ----- Se lo trova ne recupera il protocollo e lo cancella
			recuperare_id = recuperare_ids[0]
			protocollo = recuperare_obj.browse(cr, uid, recuperare_id).protocollo
			recuperare_obj.unlink(cr, uid, recuperare_id)
			return protocollo
		else:
			cr.execute('select id from ir_sequence where '
				+ test + '=%s and active=%s', (code, True,))
			res = cr.dictfetchone()
			if res:
				for line in self.browse(cr, uid, res['id'], context=context).fiscal_ids:
					if line.fiscalyear_id.id == context.get('fiscalyear_id', False):
						return super(ir_sequence, self).get_id(cr, uid,
								line.sequence_id.id, test="id", context=context)
			return super(ir_sequence, self).get_id(cr, uid, code, test, context=context)


ir_sequence()
