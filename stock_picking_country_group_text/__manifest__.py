##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2020- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

{
    "name": "Stock Picking- Report text by country group",
    "summary": "Get stock picking report text from country groups setting",
    "version": "12.0.1.0.0",
    "category": "Stock",
    "website": "https://github.com/Tawasta/stock",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["stock", "l10n_fi_country_groups", "stock_dispatch_note_report"],
    "data": [
        "views/country_group.xml",
        "report/dispatch_note.xml",
        "report/delivery_slip.xml",
        "report/stock_picking.xml", "views/menu.xml"
    ],
}
