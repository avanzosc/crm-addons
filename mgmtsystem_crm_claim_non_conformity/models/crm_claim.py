# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    def _default_claim_type(self):
        claim_type_obj = self.env["crm.claim.type"]
        if "non_conformity" in self.env.context:
            cond = [("non_conformity", "=", True)]
            claim_type = claim_type_obj.search(cond, limit=1)
            if claim_type:
                return claim_type.id
        return claim_type_obj

    claim_type = fields.Many2one(default=_default_claim_type)
