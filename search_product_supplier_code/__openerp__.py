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

{
    'name': 'Search Product Supplier Code',
    'version': '0.1',
    'category': 'Tools',
    'complexity': "easy",
    'description': 'Module used to search the product code in the supplierinfo too',
    'author': 'www.andreacometa.it',
    'website': 'http://www.andreacometa.it',
    'depends': ['product'],
    'init_xml': [],
    'update_xml': [
        'product/product_view.xml',
    ],
    'demo_xml': [],
    'test':[],
    'installable': True,
    'images': [],
}
