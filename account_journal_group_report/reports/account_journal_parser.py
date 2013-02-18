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

class account_journal_report(report_sxw.rml_parse):
	def __init__(self, cr, uid, name, context):
		super(account_journal_report, self).__init__(cr, uid, name, context=context)
		self.localcontext.update({
			'datetime': datetime,
			'time': time,
			'cr':cr,
			'uid': uid,
		})

report_sxw.report_sxw('report.webkit.account_journal_by_group',
						'account.move', 
						'account_journal_group_report/reports/account_journal_report.mako',
						parser=account_journal_report)

