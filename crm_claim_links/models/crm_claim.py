# Copyright 2014 Daniel Campos - AvanzOSC
# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, fields, models
from odoo.models import expression


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    picking_ids = fields.One2many(
        string="Stock Pickings",
        comodel_name="stock.picking",
        inverse_name="claim_id",
        copy=False,
    )
    repair_ids = fields.One2many(
        string="Repair Orders",
        comodel_name="repair.order",
        inverse_name="claim_id",
        copy=False,
    )

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        args = args or []
        if name:
            args = expression.AND(
                [
                    args,
                    expression.OR(
                        [
                            [("name", operator, name)],
                            [("code", operator, name)],
                        ]
                    ),
                ]
            )
        return super().name_search(
            name="",
            args=args,
            operator=operator,
            limit=limit,
        )

    @api.depends("name", "code")
    def _compute_display_name(self):
        for claim in self:
            display_name = claim.name
            if claim.code:
                display_name = f"[{claim.code}] {display_name}"
            claim.display_name = display_name
