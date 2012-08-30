
from osv import fields, osv

from tools.translate import _
import netsvc
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
import decimal_precision as dp

class account_invoice(osv.osv):

	_inherit = "account.invoice"

	def write(self, cr, uid, ids, values, context=None):
		result = super(account_invoice, self).write(cr, uid, ids, values, context=None)
		if type(ids) == type([]):
			for line in self.browse(cr, uid, ids[0]).invoice_line:
				if not line.invoice_line_tax_id:
					raise osv.except_osv(_('Attenzione!'), _('Impostare un\'aliquota IVA per i prodotti in cui manca!'))
		return result

account_invoice()


class account_invoice_line(osv.osv):

	_inherit = "account.invoice.line"

	def _iva_riga(self, cr, uid, ids, name, arg, context=None):
		res = {}
		for line in self.browse(cr, uid, ids, context=context):
			res[line.id] = line.invoice_line_tax_id and line.invoice_line_tax_id[0].id or False
		return res

	_columns = {
		'iva_riga' : fields.function(_iva_riga, method=True, string='Iva', type='many2one', obj='account.tax', store=False),
	}

account_invoice_line()
