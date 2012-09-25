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
{
	'name': 'Account Payment Term Enhanced',
	'version': '1.0',
	'category': 'Accounting & Finance',
	'description': """ITA: Aggiunge la possibilità di calcolare le scadenze ripartendole equamente\n
	ENG: Adds the ability to calculate maturities basing them equally""",
	'author': 'Andrea Cometa',
	'website': 'http://www.andreacometa.it',
	'depends': ['account'],
	'update_xml': [ 'account_view.xml',],
	'installable': True,
	'active': False,
	'images' : ['images/image.png'],
}

