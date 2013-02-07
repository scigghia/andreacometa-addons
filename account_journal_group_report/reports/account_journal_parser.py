# -*- coding: utf-8 -*-
##############################################################################
#    
#    Modulo realizzato da Andrea Cometa (info@andreacometa.it)
#    Compatible with OpenERP release 6.1.X
#    Copyright (C) 2012 Andrea Cometa. All Rights Reserved.
#    Email: info@andreacometa.it
#    Web site: http://www.andreacometa.it
#
##############################################################################
import time
from report import report_sxw
import inspect, os
from datetime import datetime
from osv import osv
from osv import fields

class account_journal_report(report_sxw.rml_parse):
	def invoice_date(self, cr, uid, invoice_id):
		invoice = self.pool.get('account.invoice').browse(self,cr,uid, invice_id)
		return invoice.data

	def __init__(self, cr, uid, name, context):
		super(account_journal_report, self).__init__(cr, uid, name, context=context)
		file_path = os.path.dirname(inspect.getfile(inspect.currentframe()))
		self.localcontext.update({
			'datetime': datetime,
			'time': time,
			'cr':cr,
			'uid': uid,
			'file_path':file_path,
			'invoice_date':self.invoice_date,
		})

report_sxw.report_sxw('report.account_journal_by_group',
						'account.move', 
						'account_journal_group_report/reports/account_journal_report.mako',
						parser=account_journal_report)

