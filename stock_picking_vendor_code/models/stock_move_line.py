from odoo import fields, models


class StockMoveLine(models.Model):

    _inherit = 'stock.move.line'

    vendor_code = fields.Char(
        string='Vendor code',
        compute='_compute_vendor_code',
    )

    def _compute_vendor_code(self):
        product_supplierinfo = self.env['product.supplierinfo'].sudo()
        for record in self:
            # Search pricelist items for line product
            supplierinfo = product_supplierinfo.search([
                ('product_tmpl_id', '=', record.product_id.product_tmpl_id.id),
                ('name', '=', record.picking_id.partner_id.id),
            ], limit=1)

            if supplierinfo:
                record.vendor_code = supplierinfo.product_code
