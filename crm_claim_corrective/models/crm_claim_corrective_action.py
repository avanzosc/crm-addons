# Copyright 2021 Daniel Campos - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CrmClaimCorrectiveAction(models.Model):
    _name = "crm.claim.corrective.action"
    _description = "Corrective Actions"
    _order = "sequence"

    corrective_id = fields.Many2one(
        comodel_name="crm.claim.corrective",
        string="Corrective info",
    )
    name = fields.Char(
        required=True,
    )
    sequence = fields.Integer()
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
    date_done = fields.Date()
