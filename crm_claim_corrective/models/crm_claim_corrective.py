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
        selection=[
            ("draft", "Draft"),
            ("pending", "Pending"),
            ("closed", "Closed"),
        ],
        string="Status",
        default="draft",
        copy=False,
    )

    @api.model
    def create(self, vals):
        if vals.get("name", "/") == "/":
            vals["name"] = self.env.ref(
                "crm_claim_corrective.seq_corrective_action", raise_if_not_found=False
            ).next_by_id()
        return super().create(vals)


class CrmClaimCorrectiveAction(models.Model):
    _name = "crm.claim.corrective.action"
    _description = "Corrective Actions"
    _order = "sequence"

    corrective_id = fields.Many2one(
        comodel_name="crm.claim.corrective",
        string="Corrective info",
    )
    name = fields.Char(
        string="Name",
        required=True,
    )
    sequence = fields.Integer(
        string="Sequence",
    )
    claim_id = fields.Many2one(
        comodel_name="crm.claim",
        related="corrective_id.claim_id",
        string="Claim",
        store=True,
        readonly=True,
    )
    responsible_id = fields.Many2one(
        comodel_name="res.users",
        string="Responsible",
        help="Select a Responsible",
    )
    date_planned = fields.Date(string="Planned Date")
    date_done = fields.Date(string="Date Done")
