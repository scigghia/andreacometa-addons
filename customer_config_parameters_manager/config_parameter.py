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


class ir_config_parameter(osv.osv):

	_name = 'ir.config_parameter'
	_inherit = 'ir.config_parameter'

	_columns = {
		'custom': fields.boolean('Custom'),
	}

	_defaults = {
		'custom' : False,
		}

ir_config_parameter()

