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


class account_journal_group(osv.osv):
	
	_name = 'account.journal.group'
	_description = 'Account Journal Group'

	_columns = {
		'name' : fields.char('Name', size=64),
		'journals_ids': fields.one2many('account.journal', 'group', 'Account Journals'),
	}

account_journal_group()

class account_journal(osv.osv):
	_inherit = "account.journal"
	_columns = {
		'group':fields.many2one('account.journal.group', 'Account Journal Group', 
			help="Journal Group for printing"),
	}
account_journal()

class account_move(osv.osv):
	_inherit = "account.move"
	_columns = {
		'group':fields.related('journal_id', 'group', type="many2one",
			relation="account.journal.group", string='Account Journal Group', 
			help="Journal Group for printing"),
	}
account_move()
