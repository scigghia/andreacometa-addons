# -*- encoding: utf-8 -*-
##############################################################################
#
#    Personalizzazione realizzata da Francesco OpenCode Apruzzese (f.apruzzese@andreacometa.it)
#    Compatible with OpenERP release 6.1.X
#    Copyright (C) 2012 Andrea Cometa. All Rights Reserved.
#    Email: cescoap@gmail.com, info@andreacometa.it
#    Web site: http://www.andreacometa.it
#
##########################################################################

from osv import fields, osv


class account_invoice(osv.osv):

	_name = "account.invoice"
	_inherit = "account.invoice"

	_columns = {
		'immediate' : fields.boolean('Immediate'),
	}

account_invoice()
