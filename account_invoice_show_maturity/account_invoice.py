# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Andrea Cometa - Perito informatico
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


class account_invoice(osv.osv):

    _inherit = "account.invoice"

    def _maturity(self, cr, uid, ids, filed_name, arg, context=None):
        res = {}
        for o in self.browse(cr, uid, ids, context):
            if not o.id in res:
                res[o.id] = []
            if o.move_id and o.move_id.line_id:
                for line in o.move_id.line_id:
                    if line.date_maturity:
                        res[o.id].append(line.id)
        return res

    _columns = {
        "maturity_ids": fields.function(
            _maturity, type="one2many", store=False,
            relation="account.move.line", method=True)
        }
