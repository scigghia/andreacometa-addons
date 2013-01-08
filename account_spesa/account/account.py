# -*- coding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2013 Francesco OpenCode Apruzzese (<cescoap@gmail.com>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
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
from tools.translate import _

class account_spesa(osv.osv):

	_name = "account.spesa"
	_description = "Account expenses"

	_columns = {
		'name' : fields.char('Name', size=64),
		'account_id' : fields.many2one('account.account','Account'),
		'price' : fields.float('Price'),
		'tax_id': fields.many2one('account.tax','Tax'),
		'type' : fields.selection(
			(('bank', 'Bank'),('delivery', 'Delivery')),
			'Type'),
		}

account_spesa()


class account_payment_term_line(osv.osv):

	_name = "account.payment.term.line"
	_inherit = "account.payment.term.line"
	
	_columns = {
		'spesa_id' : fields.many2one('account.spesa','Expense'),
		}

account_payment_term_line()
