# -*- coding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2013 Francesco OpenCode Apruzzese (<cescoap@gmail.com>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
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

from osv import fields, osv
from tools.translate import _

class product_product(osv.osv):

	_name = "product.product"
	_inherit = 'product.product'

	def _uom_diverge(self, cr, uid, ids, name, arg, context=None):
		res = {}
		products = self.browse(cr, uid, ids)
		for product in products:
			diverge = False
			uom_id = product.uom_id and product.uom_id.category_id and product.uom_id.category_id.id or False
			uom_po_id = product.uom_po_id and product.uom_po_id.category_id and product.uom_po_id.category_id.id or False
			if uom_id and uom_po_id and uom_id != uom_po_id:
				diverge = True
			res.update({product.id:diverge})
		return res

	_columns = {
		'uom_categ_diverge' : fields.function(_uom_diverge, type='boolean', method=True, store=True),
		}

product_product()
