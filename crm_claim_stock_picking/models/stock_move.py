# Copyright 2021 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class StockMove(models.Model):
    _inherit = 'stock.move'

    def button_create_claim(self):
        today = fields.Date.today()
        claim_vals = {
            'picking_id': self.picking_id.id,
            'name': u'{} {} {}'.format(
                today, self.picking_id.partner_id.name, self.product_id.name),
            'partner_id': self.picking_id.partner_id.id,
            'model_ref_id': '%s,%s' % ('product.product', self.product_id.id),
            'second_model_ref_id': '%s,%s' % ('stock.move', self.id)
            }
        self.env['crm.claim'].create(claim_vals)
