# Copyright 2026 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import _, exceptions, fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    repair_sale_order_id = fields.Many2one(
        string="Repair Sale Order", comodel_name="sale.order"
    )

    def action_create_sale_order_repair(self):
        if not self.partner_id:
            raise exceptions.ValidationError(_("You must enter the partner"))
        values = self._catch_sale_order_values()
        self.repair_sale_order_id = self.env["sale.order"].create(values).id
        return True

    def _catch_sale_order_values(self):
        cond = [("is_repair", "=", True)]
        repair_type = self.env["sale.order.type"].search(cond, limit=1)
        if not repair_type:
            raise exceptions.ValidationError(
                _("The repair sales order type could not be found")
            )
        vals = {
            "partner_id": self.partner_id.id,
            "type_id": repair_type.id,
            "crm_claim_id": self.id,
        }
        return vals
