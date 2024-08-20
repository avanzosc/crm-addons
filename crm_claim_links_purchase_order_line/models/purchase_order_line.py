# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    claims = fields.Char(compute="_compute_claims", store=True, copy=False)

    @api.depends(
        "move_ids",
        "move_ids.picking_id",
        "move_ids.picking_id.claim_id",
        "move_ids.picking_id.claim_id.name",
    )
    def _compute_claims(self):
        for line in self:
            claims = ""
            moves = line.move_ids.filtered(lambda x: x.picking_id)
            for move in moves:
                if (
                    move.picking_id.claim_id
                    and move.picking_id.claim_id.name not in claims
                ):
                    if not claims:
                        claims = move.picking_id.claim_id.name
                    else:
                        claims = "%(claims)s, %(name)s" % {
                            "claims": claims,
                            "name": move.picking_id.claim_id.name,
                        }
            line.claims = claims
