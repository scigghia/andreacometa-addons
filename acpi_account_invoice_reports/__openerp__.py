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
    "name": "Just Another Account Invoice Reports",
    "description": """
    [ENG] Generic Report for account invoice to separate Immediate and Deferred Invoice
    [ITA] Report Generici per ottenere stampe separate di fatture immediate e differite
    
    ==============================
    [ENG] ATTENTION: To obtain a better report, add a webkit logo record with name 'Logo'
    and an image with max width 300px
    [ITA] ATTENZIONE: Per ottenere una migliore resa dei report, creare una nuovo webkit logo
    con nome 'Logo' ed inserire un'immagine con larghezza massima 300px
    """,
    "version": "0.1",
    "depends": ["report_webkit", "l10n_it", "l10n_it_fiscalcode"],
    "category": "Reporting",
    "author": "www.andreacometa.it",
    "url": "http://www.andreacometa.it",
    "data": [
        "acpi_reports.xml",
     ],
    "installable": True,
    "auto_install": False,
    "certificate": "",
    'images': ['images/image.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
