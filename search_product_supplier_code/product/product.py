#!/usr/bin/python
# -*- coding: utf-8 -*-
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

from osv import osv, fields


class product_product(osv.osv):

	_name = 'product.product'
	_inherit = 'product.product'

	def name_search(self, cr, user, name, args=None, operator='ilike', context=None, limit=100):
		if name:
			if args:
				args = ['|', ('suppliers_code', operator, '%' + name + '%')] + args
			else:
				args = ['|', ('suppliers_code', operator, '%' + name + '%')]
		res = super(product_product,self).name_search(cr, user, name, args, operator='ilike', context=None, limit=100)
		return res

	def _suppliers_code(self, cr, uid, ids, name, arg, context=None):
		res = {}
		prds = self.browse(cr, uid, ids)
		for prd in prds:
			code = ''
			for line in prd.seller_ids:
				code = '%s %s' % (code, line.product_code)
			res[prd.id] = code
		return res

	_columns = {
		'suppliers_code': fields.function(_suppliers_code, type='char', size=256, string='Supplier Code', store=True),
		}

product_product()
