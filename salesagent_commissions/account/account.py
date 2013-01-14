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
import time


class account_invoice(osv.osv):

	_inherit = "account.invoice"

	def create(self, cr, uid, vals, context=None):
		invoice_id = super(account_invoice, self).create(cr, uid, vals, context)
		# QUI DOVRA RICHIAMARE L?AGENTE PARTENDO DAL CLIENTE
		#partner = self.pool.get('res.partner').read(cr, uid, partner_id, ['salesagent_for_customer_id'])
		#agente_id = partner['salesagent_for_customer_id']
		return invoice_id

	def _total_commission(self, cr, uid, ids, name, arg, context=None):
		res = {}
		for invoice in self.browse(cr, uid, ids, context=context):
			if invoice.type == 'out_invoice':
				sign = 1
			elif invoice.type == 'out_refund':
				sign = -1
			else:
				sign = 0
			total_commission = 0.0 
			for line in invoice.invoice_line:
				total_commission += (line.commission * sign)
			res[invoice.id] = total_commission
		return res

	def onchange_partner_id(self, cr, uid, ids, type, partner_id, date_invoice=False, payment_term=False, partner_bank_id=False, company_id=False):
		if not partner_id:
			return {}
		partner = self.pool.get('res.partner').read(cr, uid, partner_id, ['salesagent_for_customer_id'])
		salesagent_id = partner['salesagent_for_customer_id']
		res = super(account_invoice, self).onchange_partner_id(cr, uid, ids, type, partner_id, date_invoice, payment_term, partner_bank_id, company_id)
		res['value']['salesagent_id'] = salesagent_id
		return res

	_columns = {
		'salesagent_id' : fields.many2one('res.partner', 'Salesagent'),
		'commission' : fields.function(_total_commission, method=True, string='Commission', type='float', store=False),
		'paid_commission' : fields.boolean('Paid'),
		'paid_date' : fields.date('Commission Payment Date'),
	}

account_invoice()


class account_invoice_line(osv.osv):

	_inherit = "account.invoice.line"

	def _commission(self, cr, uid, ids, name, arg, context=None):
		res = {}
		salesagent_common_obj = self.pool.get('salesagent.common')
		for line in self.browse(cr, uid, ids, context=context):
			if line.invoice_id.type == 'out_invoice':
				sign = 1
			elif line.invoice_id.type == 'out_refund':
				sign = -1
			else:
				sign = 0
			res[line.id] = {'commission':0.0, 'commission_percentage':0.0}
			if not line.no_commission:
				# ----- if a paid commission exist, show it or calculate it
				if line.paid_commission_value:
					comm = line.paid_commission_value
					comm_percentage = line.paid_commission_percentage_value
				else:
					comm = sign * salesagent_common_obj.commission_calculate(cr, uid, 'account.invoice.line', line.id)
					comm_percentage = salesagent_common_obj.recognized_commission(cr, uid, line.partner_id and line.partner_id.id or False, line.salesagent_id and line.salesagent_id.id or False, line.product_id and line.product_id.id or False)
				res[line.id]['commission'] = comm
				res[line.id]['commission_percentage'] = comm_percentage
				if comm != 0:
					self.write(cr, uid, [line.id, ], {'commission_presence':True})
				else:
					self.write(cr, uid, [line.id, ], {'commission_presence':False})
			else:
				self.write(cr, uid, [line.id, ], {'commission_presence':False})
		return res

	_columns = {
		'reconciled' : fields.related('invoice_id', 'reconciled', type='boolean',string='Reconciled'),
		'no_commission' : fields.boolean('No Commission', help='Indicates if the commission __ NOT__ must be calculated for this time!'),
		'commission_presence' : fields.boolean('Commission Presence'),
		'commission_percentage' : fields.function(_commission, method=True, string='Comm. Percentage', type='float', store=False, multi='comm'),
		'commission' : fields.function(_commission, method=True, string='Provv. Total', type='float', store=False, multi='comm'),
		'salesagent_id' : fields.related('invoice_id', 'salesagent_id', type='many2one', relation='res.partner', string='Salesagent',
			store=False),
		'partner_id' : fields.related('invoice_id', 'partner_id', type='many2one', relation='res.partner', string='Customer', store=True),
		'date_invoice' : fields.related('invoice_id', 'date_invoice', type='date', string='Invoice Date',
			store=False),
		'paid_commission_value' : fields.float('Paid Commission'),
		'paid_commission_percentage_value' : fields.float('Paid Commission Percentage'),
		'paid_commission' : fields.boolean('Paid'),
		'payment_commission_date' : fields.date('Payment Commission Date'),
		'payment_commission_note' : fields.char('Payment Commission Note', size=128),
	}

	_defaults = {
		'no_commission' : False,
		'paid_commission_value' : 0.0,
		}

account_invoice_line()
