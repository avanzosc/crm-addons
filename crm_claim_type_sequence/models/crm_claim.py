# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if (
                vals.get("code", "/") == "/"
                and "claim_type" in vals
                and vals.get("claim_type", False)
            ):
                claim_type = self.env["crm.claim.type"].browse(vals.get("claim_type"))
                if claim_type.sequence_id:
                    vals["code"] = claim_type.sequence_id.next_by_id()
        return super().create(vals_list)
