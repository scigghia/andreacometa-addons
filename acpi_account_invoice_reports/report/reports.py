import time
from report import report_sxw
from osv import osv
import inspect, os
from datetime import datetime
from math import ceil

class report_webkit(report_sxw.rml_parse):

    def page_number(self, lines, row_limit):
        if not lines or not row_limit:
            return 0
        division = float(len(lines)) / float(row_limit)
        pn = int(ceil(division))
        return pn

    def newlined_text(self, text):
        if text:
            return text.replace('\n', '<br/>')

    def __init__(self, cr, uid, name, context):
        super(report_webkit, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'datetime': datetime,
            'time': time,
            'cr':cr,
            'uid': uid,
            'newlined_text':self.newlined_text,
            'page_number':self.page_number
        })

report_sxw.report_sxw('report.acpi.immediate.invoice',
                       'account.invoice', 
                       'acpi_account_invoice_reports/report/immediate.mako',
                       parser=report_webkit)

report_sxw.report_sxw('report.acpi.deferred.invoice',
                       'account.invoice', 
                       'acpi_account_invoice_reports/report/deferred.mako',
                       parser=report_webkit)
