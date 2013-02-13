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

import time
from report import report_sxw
from datetime import datetime
from osv import osv, fields
import pooler

class account_journal_report(report_sxw.rml_parse):
	def _invoice_date(self, move_id):
		print "CARNE"
		#invoice_id = pooler.get_pool(self.cr.dbname).get('account.invoice').search(self, self.cr, self.uid, [('move_id', '=', move_id)])
		#invoice = pooler.get_pool(self.cr.dbname).get('account.invoice').browse(self, self.cr, self.uid, invoice_id)
		#return invoice.date_invoice
		return True
	
	def prova(self):
		return "ciao"

	def __init__(self, cr, uid, name, context):
		super(account_journal_report, self).__init__(cr, uid, name, context=context)
		#file_path = os.path.dirname(inspect.getfile(inspect.currentframe()))
		self.localcontext.update({
			'datetime': datetime,
			'time': time,
			'cr':cr,
			'uid': uid,
			#'file_path':file_path,
			#'invoice_date':self._invoice_date,
			'prova':self.prova,
		})

report_sxw.report_sxw('report.account_journal_by_group',
						'account.move', 
						'account_journal_group_report/reports/account_journal_report.mako',
						parser=account_journal_report)

