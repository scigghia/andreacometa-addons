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
import decimal_precision as dp
from tools.translate import _

class account_account(osv.osv):
	_inherit = 'account.account'
	
	_columns={
		'flag_discount':fields.boolean("Discount Flag", 
			help="NOTE: Use it for only one account. Is the account for discount in move line")
	}
	_defaults={
		'flag_discount' : False,
	}
account_account()

class account_invoice(osv.osv):
	_inherit = 'account.invoice'

	def _amount_all(self, cr, uid, ids, name, args, context=None):
		res = super(account_invoice, self)._amount_all(cr, uid, ids, name, args, context)
		for invoice in self.browse(cr, uid, ids, context=context):
			if invoice.global_discount > 0.0:
				sconto = (100.00 - invoice.global_discount) / 100.00
				res[invoice.id]['amount_untaxed'] *= sconto
				#res[invoice.id]['amount_tax'] *= sconto
				res[invoice.id]['amount_total'] = res[invoice.id]['amount_tax'] + res[invoice.id]['amount_untaxed']
		return res

	def _get_invoice_line(self, cr, uid, ids, context=None):
		result = {}
		for line in self.pool.get('account.invoice.line').browse(cr, uid, ids, context=context):
			result[line.invoice_id.id] = True
		return result.keys()

	def _get_invoice_tax(self, cr, uid, ids, context=None):
		result = {}
		for tax in self.pool.get('account.invoice.tax').browse(cr, uid, ids, context=context):
			result[tax.invoice_id.id] = True
		return result.keys()

	def _global_discount_amount(self, cr, uid, ids, field_name, arg, context):
		res={}
		for inv in self.browse(cr, uid, ids):
			amt=0.0
			for line in inv.invoice_line:
				amt+=line.global_discount_amount
			res[inv.id]=amt
		return res

	_columns = {
		'global_discount' : fields.float('Global Discount', states={'draft':[('readonly',False)]}, 
			help="Invoice Global Discount [0-100]"),
		'global_discount_amount': fields.function(_global_discount_amount, method=True, 
			type="float", string="Global Discount Amount"),
		'amount_untaxed': fields.function(_amount_all, digits_compute=dp.get_precision('Account'), string='Untaxed',
			store={
				'account.invoice': (lambda self, cr, uid, ids, c={}: ids, ['invoice_line'], 20),
				'account.invoice.tax': (_get_invoice_tax, None, 20),
				'account.invoice.line': (_get_invoice_line, ['price_unit','invoice_line_tax_id','quantity','discount','invoice_id'], 20),
			},
			multi='all'),
		'amount_tax': fields.function(_amount_all, digits_compute=dp.get_precision('Account'), string='Tax',
			store={
				'account.invoice': (lambda self, cr, uid, ids, c={}: ids, ['invoice_line'], 20),
				'account.invoice.tax': (_get_invoice_tax, None, 20),
				'account.invoice.line': (_get_invoice_line, ['price_unit','invoice_line_tax_id','quantity','discount','invoice_id'], 20),
			},
			multi='all'),
		'amount_total': fields.function(_amount_all, digits_compute=dp.get_precision('Account'), string='Total',
			store={
				'account.invoice': (lambda self, cr, uid, ids, c={}: ids, ['invoice_line'], 20),
				'account.invoice.tax': (_get_invoice_tax, None, 20),
				'account.invoice.line': (_get_invoice_line, ['price_unit','invoice_line_tax_id','quantity','discount','invoice_id'], 20),
			},
			multi='all'),
	}

	def finalize_invoice_move_lines(self, cr, uid, invoice_browse, move_lines):
		"""finalize_invoice_move_lines(cr, uid, invoice, move_lines) -> move_lines
		Hook method to be overridden in additional modules to verify and possibly alter the
		move lines to be created by an invoice, for special cases.
		:param invoice_browse: browsable record of the invoice that is generating the move lines
		:param move_lines: list of dictionaries with the account.move.lines (as for create())
		:return: the (possibly updated) final move_lines to create for this invoice
		"""
		#if invoice_browse.global_discount > 0.00:
		#temp = {}
		account_discount_id = self.pool.get('account.account').search(cr,uid,[('flag_discount','=',True)])
		if account_discount_id:
			account_discount_id = account_discount_id[0]
		else:
			raise osv.except_osv(_('Warning !'), _('There must be, an account whit flag_discount=True, to compute move lines!'))
		sconto = (100.00 - invoice_browse.global_discount) / 100.00
		total_amount = 0.0
		for m in move_lines:
			if m[2]['credit'] > 0.0:
				total_amount += m[2]['credit']
		new_line = {'analytic_account_id': False, 'tax_code_id': False, 'analytic_lines': [],
			'tax_amount': False, 'name': u'Sconto Globale', 'ref': '',
			'analytics_id': False, 'currency_id': False, 'debit': total_amount - invoice_browse.amount_total ,
			'product_id': False, 'date_maturity': False, 'credit': False, 'date': move_lines[0][2]['date'],
			'amount_currency': 0, 'product_uom_id': False, 'quantity': 1, 'partner_id': move_lines[0][2]['partner_id'],
			'account_id': account_discount_id}
		num_lines=0
		for m in move_lines:
			if m[2]['debit'] > 0.0:
				num_lines+=1
		discount_amount = (total_amount - invoice_browse.amount_total) / num_lines
		#print num_lines, discount_amount
		for m in move_lines:
			if m[2]['debit'] > 0.0:
				#print m[2]['debit']
				m[2]['debit'] -= discount_amount
		#move_lines += [(0,0,new_line)]
		precisione = self.pool.get('decimal.precision').precision_get(cr, 1, 'Account')
		debit=credit=0.0
		for m in move_lines:
			#print m[2]['debit'], "\t", m[2]['credit']
			debit += round(m[2]['debit'], precisione)
			credit += round(m[2]['credit'], precisione)
		precision_diff = round(credit - debit, precisione)
		#print precision_diff
		new_line['debit']=precision_diff
		move_lines += [(0,0,new_line)]
		return move_lines

account_invoice()

class account_invoice_tax(osv.osv):
	_inherit = "account.invoice.tax"

	def compute(self, cr, uid, invoice_id, context=None):
		tax_grouped = super(account_invoice_tax, self).compute(cr, uid, invoice_id, context=None)
		inv = self.pool.get('account.invoice').browse(cr, uid, invoice_id, context=context)
		sconto = (100.00 - inv.global_discount) / 100.00

		for t in tax_grouped.values():
			t['base'] *= sconto
			t['amount'] *= sconto
			t['base_amount'] *= sconto
			t['tax_amount'] *= sconto
		return tax_grouped

account_invoice_tax()
