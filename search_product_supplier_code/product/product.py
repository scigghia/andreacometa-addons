# -*- coding: utf-8 -*-
#       
#       Copyright 2012 Francesco OpenCode Apruzzese <cescoap@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       

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
