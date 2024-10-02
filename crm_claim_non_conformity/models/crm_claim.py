# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    def _default_claim_type(self):
        claim_type_obj = self.env["crm.claim.type"]
        if "non_conformity" in self.env.context and self.env.context.get(
            "non_conformity"
        ):
            cond = [("non_conformity", "=", True)]
            claim_type = claim_type_obj.search(cond, limit=1)
            if claim_type:
                return claim_type.id
        return claim_type_obj

    def _default_non_conformity(self):
        if "non_conformity" in self.env.context:
            return self.env.context.get("non_conformity")
        return False

    claim_type = fields.Many2one(default=_default_claim_type)
    non_conformity = fields.Boolean(
        string="Is Non Conformity?", default=_default_non_conformity
    )

    @api.onchange("non_conformity")
    def onchange_non_conformity(self):
        return {
            "domain": {"claim_type": [("non_conformity", "=", self.non_conformity)]}
        }
