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

	def _suppliers_code_search(self, cr, uid, obj, name, args, context):
		for arg in args:
			if arg[0] == 'suppliers_code' and arg[1] == 'ilike':
				# ----- Obtain all the products ids
				ids = self.search(cr, uid, [('active', '=', True)], context=context)
				prds = self.browse(cr, uid, ids, context)
				prd_available = []
				for prd in prds:
					if arg[2] in prd.suppliers_code:
						prd_available.append(prd.id)
				return [('id', 'in', prd_available)]
		return []

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
		'suppliers_code': fields.function(_suppliers_code, type='char', size=128, string='Supplier Code', fnct_search=_suppliers_code_search, store=False),
		}

product_product()
