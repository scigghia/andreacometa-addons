# -*- coding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) 2012 Francesco OpenCode Apruzzese (<cescoap@gmail.com>)
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
	_inherit = "product.product"

	# ----- One earning function
	def _earning(self, cr, uid, ids, name, arg, context=None):
		res = {}
		prds = self.browse(cr, uid, ids)
		for prd in prds:
			earn_percentage = 0.00
			if prd.list_price and prd.standard_price:
				earn_percentage = (prd.list_price / prd.standard_price) - 1
			earn_fixed = prd.list_price - prd.standard_price
			res[prd.id] = {'earning_percentage': earn_percentage, 'earning_fixed': earn_fixed}
		return res

	_columns = {
		'earning_percentage' : fields.function(_earning, string="Percentage Earning", type='float', store=False, multi='earn'),
		'earning_fixed' : fields.function(_earning, string="Fixed Earning", type='float', store=False, multi='earn'),
		}

product_product()
