# -*- encoding: utf-8 -*-
##############################################################################
#
#    Addon realizzato da Andrea Cometa
#    Compatible with OpenERP release 6.1.0
#    Copyright (C) 2012 Andrea Cometa. All Rights Reserved.
#    Email: info@andreacometa.it
#    Web site: http://www.andreacometa.it
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
	}

	_defaults = {
		'maturities' : 1,
		'days': 0,
		'days2' : 0,
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
			next_date = datetime.strptime(date_ref, '%Y-%m-%d')
			#print "### %i %i %i" % (pt.maturities, pt.days, pt.days2)
			for i in range(0, pt.maturities):
				#print next_date, pt.days2
				if i==0:
					if pt.days2 < 0:
						next_first_date = next_date + relativedelta(day=1,months=1) #Getting 1st of next month
						next_date = next_first_date + relativedelta(days=pt.days2)
					if pt.days2 > 0:
						next_date += relativedelta(day=pt.days2, months=1)
				else:
					next_date += relativedelta(days=pt.days)
				if i < pt.maturities-1:
					#print "### STEP"
					result.append( (next_date.strftime('%Y-%m-%d'), single_amount) )
					amount -= single_amount
				else: # last round
					#print "### LAST"
					result.append( (next_date.strftime('%Y-%m-%d'), amount) )
				#print "### %i, %f, %f" % (i, single_amount, amount)
		else:
			for line in pt.line_ids:
				if line.value == 'fixed':
					amt = round(line.value_amount, prec)
				elif line.value == 'procent':
					amt = round(value * line.value_amount, prec)
				elif line.value == 'balance':
					amt = round(amount, prec)
				if amt:
					next_date = (datetime.strptime(date_ref, '%Y-%m-%d') + relativedelta(days=line.days))
					if line.days2 < 0:
						next_first_date = next_date + relativedelta(day=1,months=1) #Getting 1st of next month
						next_date = next_first_date + relativedelta(days=line.days2)
					if line.days2 > 0:
						next_date += relativedelta(day=line.days2, months=1)
					result.append( (next_date.strftime('%Y-%m-%d'), amt) )
					amount -= amt
		return result

account_payment_term()

