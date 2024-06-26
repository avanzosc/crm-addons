# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    crm_claim_tag_ids = fields.Many2many(
        string="Tags", comodel_name="crm.claim.tag", copy=False
    )
