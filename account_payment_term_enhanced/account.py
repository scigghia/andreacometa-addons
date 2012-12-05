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
from datetime import datetime
from dateutil.relativedelta import relativedelta

class account_payment_term(osv.osv):
	_inherit = "account.payment.term"

	_columns = {
		'fairly' : fields.boolean("Distribute fairly"),
		'days': fields.integer('Number of Days', required=True, 
			help="Number of days between every maturity from the day of month." \
			"If Date=15/01, Number of Days=22, Day of Month=-1, then the due date is 28/02."),
		'days2': fields.integer('Day of the Month', required=True, 
			help="Day of the month, set -1 for the last day of the current month. If it's positive, it gives the day of the next month. Set 0 for net days (otherwise it's based on the beginning of the month)."),
		'maturities' : fields.integer("Number of maturities", 
			help="Number of maturities to divide the total amount"),
		'start_day': fields.integer('Start Day', required=True, help="Start Day of the month, set -1 for the last day of the current month. If it's positive, it gives the day of the next month. Set 0 for net days (otherwise it's based on the beginning of the month)."),
	}

	_defaults = {
		'maturities' : 1,
		'days': 0,
		'days2' : 0,
		'start_day' : 0,
		'fairly' : False,
	}

	def compute(self, cr, uid, id, value, date_ref=False, context=None):
		if not date_ref:
			date_ref = datetime.now().strftime('%Y-%m-%d')
		pt = self.browse(cr, uid, id, context=context)
		amount = value
		result = []
		obj_precision = self.pool.get('decimal.precision')
		prec = obj_precision.precision_get(cr, uid, 'Account')
		# added by me
		if pt.fairly:
			single_amount = round(amount / pt.maturities, prec)
			if pt.start_day < 0:
				start_date = datetime.strptime(date_ref, '%Y-%m-%d') + relativedelta(day=1,months=1) + relativedelta(days=pt.start_day)
			else:
				start_date = datetime.strptime(date_ref, '%Y-%m-%d') + relativedelta(days=pt.start_day, months=0)
			print "data iniziale: %s\n" % start_date

			for i in range(0, pt.maturities):
				if pt.maturities>1:
					next_date = (start_date + relativedelta(days=pt.days * (i+1)))
					if pt.days2 < 0:
						next_first_date = next_date + relativedelta(day=1,months=1) #Getting 1st of next month
						next_date = next_first_date + relativedelta(days=pt.days2)
					if pt.days2 > 0: # numero giorno in cui farlo scadere
						next_date += relativedelta(day=pt.days2, months=1)
					print "data scadenza: %s\n" % next_date
				else:
					next_date = start_date

				if i < pt.maturities-1:
					result.append( (next_date.strftime('%Y-%m-%d'), single_amount) )
					amount -= single_amount
				else: # last round
					result.append( (next_date.strftime('%Y-%m-%d'), amount) )
		else:
			for line in pt.line_ids:
				if line.value == 'fixed':
					amt = round(line.value_amount, prec)
				elif line.value == 'procent':
					amt = round(value * line.value_amount, prec)
				elif line.value == 'balance':
					amt = round(amount, prec)
				if amt:
					if line.start_day < 0:
						start_date = datetime.strptime(date_ref, '%Y-%m-%d') + relativedelta(day=1,months=1) + relativedelta(days=line.start_day)
					else:
						start_date = datetime.strptime(date_ref, '%Y-%m-%d') + relativedelta(days=line.start_day, months=1)
					next_date = (start_date + relativedelta(days=line.days) )
					if line.days2 < 0:
						next_first_date = next_date + relativedelta(day=1,months=1) #Getting 1st of next month
						next_date = next_first_date + relativedelta(days=line.days2)
					if line.days2 > 0:
						next_date += relativedelta(day=line.days2, months=1)
					result.append( (next_date.strftime('%Y-%m-%d'), amt) )
					amount -= amt
		return result

account_payment_term()

class account_payment_term_line(osv.osv):
	_inherit = 'account.payment.term.line'

	_columns = {
		'start_day': fields.integer('Start Day', required=True, help="Start Day of the month, set -1 for the last day of the current month. If it's positive, it gives the day of the next month. Set 0 for net days (otherwise it's based on the beginning of the month)."),
	}
	_defaults = {
		'start_day' : 0,
	}
account_payment_term_line()
