import base64
import urllib.request

from odoo import fields, http, models


class StockPicking(models.Model):

    _inherit = "stock.picking"

    barcode = fields.Binary(string="Barcode URL", compute="_barcode",)

    barcode_url = fields.Char(string="Barcode URL", compute="_barcode_url",)

    def _barcode(self):
        if isinstance(self.barcode_url, str) and len(self.barcode_url) > 0:
            img = urllib.request.urlopen(self.barcode_url).read()
            self.barcode = base64.b64encode(img)

    def _barcode_url(self, code="Code128"):
        if isinstance(self.name, str) and len(self.name) > 0:
            self.barcode_url = "{}{}{}{}{}".format(
                http.request.env["ir.config_parameter"].get_param("web.base.url"),
                "/report/barcode/",
                code,
                "/",
                self.name,
            )
        else:
            self.barcode__url = ""
