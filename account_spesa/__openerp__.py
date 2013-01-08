# -*- coding: utf-8 -*-
##############################################################################
#    
#    Copyright (C) {year} {developer} (<{mail}>)
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

{
    'name': "Expenses manage for account",
    'version': '1.0',
    'category': 'Account',
    'description': """
        Manage the expenses rof the account payment terms
    """,
    'author': 'www.andreacometa.it',
    'website': 'http://www.andreacometa.it',
    'license': 'AGPL-3',
    "depends" : ['account'],
    "init_xml" : [],
    "update_xml" : [
        'account/account_view.xml'
    ],
    "demo_xml" : [],
    "active": False,
    "installable": True
}
