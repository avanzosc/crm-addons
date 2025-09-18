# Copyright 2025 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class MrpProductionControl(models.Model):
    _inherit = "mrp.production.control"

    claim_id = fields.Many2one(string="Claim", comodel_name="crm.claim", copy=False)
    claim_categ_id = fields.Many2one(
        string="Claim Category",
        comodel_name="crm.claim.category",
        related="claim_id.categ_id",
        store=True,
        copy=False,
    )
    claim_type = fields.Many2one(
        string="Claim Type",
        comodel_name="crm.claim.type",
        related="claim_id.claim_type",
        store=True,
        copy=False,
    )
    claim_user_id = fields.Many2one(
        comodel_name="res.users",
        string="Claim Responsible",
        related="claim_id.user_id",
        store=True,
        copy=False,
    )
