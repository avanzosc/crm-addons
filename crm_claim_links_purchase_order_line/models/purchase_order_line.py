# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    claim_id = fields.Many2one(
        string="Claim", comodel_name="crm.claim",
        compute="_compute_claim_id", store=True, copy=False
    )

    @api.depends("move_ids", "move_ids.picking_id",
                 "move_ids.picking_id.claim_id")
    def _compute_claim_id(self):
        for line in self:
            claim_id = False
            if (line.move_ids and line.move_ids[0].picking_id and
                    line.move_ids[0].picking_id.claim_id):
                claim_id = line.purchase_move_ids[0].picking_id.claim.id
            line.claim_id = claim_id
