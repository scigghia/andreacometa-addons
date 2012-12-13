# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2012 Andrea Cometa - Perito informatico (http://www.andreacometa.it)
# All Right Reserved
#
# Author : Andrea Cometa (<info@andreacometa.it>)
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
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
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: