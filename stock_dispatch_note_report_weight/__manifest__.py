##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2020 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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
    "name": "Stock Dispatch Note Template Weight",
    "summary": """Calculate the total weight on stock dispatch note:
    line_pack.weight + line_pack.shipping_weight""",
    "version": "12.0.1.0.0",
    "category": "Reporting",
    "website": "https://github.com/Tawasta/stock",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["stock_dispatch_note_report"],
    "data": [
        "report/report_stock_dispatch_weight.xml",
    ],
}
