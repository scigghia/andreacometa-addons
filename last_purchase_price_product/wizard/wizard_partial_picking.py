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

from osv import osv

class partial_picking(osv.osv_memory):

	_inherit = 'stock.partial.picking'

	def do_partial(self, cr, uid, ids, context=None):
		if context is None:
			context = {} 
		res = super(partial_picking, self).do_partial(cr, uid, ids, context=context)
		pick_obj = self.pool.get('stock.picking')
		purchase_obj = self.pool.get('purchase.order')
		picking_ids = context.get('active_ids', False)
		partial = self.browse(cr, uid, ids[0], context=context)
		pick_list = pick_obj.browse(cr, uid, picking_ids, context=context)
		for pick in pick_list:
			if pick.type == 'in' and pick.origin:
				order_ids = purchase_obj.search(cr, uid, [('name','=',pick.origin)], limit=1)
				for order_id in order_ids:
					order = purchase_obj.browse(cr, uid, order_id)
					for move in partial.move_ids:
						if move.product_id.cost_method == 'lpp':
							product_cost = 0.0
							for line in order.order_line:
								if line.product_id.id == move.product_id.id:
									product_cost = line.price_unit
							self.pool.get('product.product').write(cr, uid, [move.product_id.id], {'standard_price': product_cost})
		return res

partial_picking()
