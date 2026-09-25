# Copyright 2021 Daniel Campos - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CrmClaimCorrective(models.Model):
    _name = "crm.claim.corrective"
    _description = "Claim Corrective"

    name = fields.Char(
        string="Sequence",
        default="/",
        required=True,
    )
    claim_id = fields.Many2one(
        comodel_name="crm.claim",
        string="Claim",
        help="Select a Claim",
        copy=False,
        readonly=True,
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        related="claim_id.partner_id",
        string="Customer",
        store=True,
        readonly=True,
    )
    corrective_action_ids = fields.One2many(
        comodel_name="crm.claim.corrective.action",
        inverse_name="corrective_id",
        string="Corrective Actions",
    )
    state = fields.Selection(
        selection=[("draft", "Draft"), ("pending", "Pending"), ("closed", "Closed")],
        string="Status",
        default="draft",
        copy=False,
    )

    @api.model_create_multi
    def create(self, vals_list):
        sequence = self.env.ref(
            "crm_claim_corrective.seq_corrective_action", raise_if_not_found=False
        )
        for vals in vals_list:
            if vals.get("name", "/") == "/":
                vals["name"] = sequence.next_by_id()
        return super().create(vals_list)
