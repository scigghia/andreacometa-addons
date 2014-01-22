# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2012 Andrea Cometa All Rights Reserved.
#                       www.andreacometa.it
#                       openerp@andreacometa.it
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by
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


class account_invoice(osv.osv):

    _inherit = "account.invoice"

    def action_number(self, cr, uid, ids, context=None):
        res = super(account_invoice, self).action_number(cr, uid, ids,
                                                         context=None)
        product_obj = self.pool.get('product.product')
        for inv in self.browse(cr, uid, ids, context):
            # ----- Keep only supplier invoice
            if inv.type != 'in_invoice':
                continue
            for line in inv.invoice_line:
                # ----- keep only line with product
                if line.product_id and line.product_id.cost_method == 'lip':
                    product_obj.write(cr, uid, [line.product_id.id],
                                      {'standard_price': line.price_unit})
        return res


account_invoice()
