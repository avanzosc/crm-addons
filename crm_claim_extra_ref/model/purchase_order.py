# Copyright 2026 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import _, exceptions, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def unlink(self):
        claim_obj = self.env["crm.claim"]
        for purchase in self:
            ref = ("purchase.order,%(purchase_id)s") % {
                "purchase_id": purchase.id,
            }
            claim = claim_obj.search([("model_ref_id", "=", ref)])
            if not claim:
                claim = claim_obj.search([("ref2", "=", ref)])
            if not claim:
                claim = claim_obj.search([("ref3", "=", ref)])
            if claim:
                error = _(
                    "You cannot delete the purchase order: %(purchase_name)s, "
                    "because it is being used in the claim: %(claim_name)s."
                ) % {"purchase_name": purchase.name, "claim_name": claim.code}
                raise exceptions.ValidationError(error)
        return super().unlink()
