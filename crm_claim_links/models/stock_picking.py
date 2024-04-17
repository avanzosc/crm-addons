# Copyright 2014 Daniel Campos - AvanzOSC
# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import _, exceptions, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    claim_id = fields.Many2one(
        string="Claim", comodel_name="crm.claim", copy=False
    )

    def action_stock_return_picking(self):
        context = self.env.context.copy()
        for picking in self:
            if not picking.claim_id:
                raise exceptions.ValidationError(
                    _("Selected Picking has no claim" " order assigned")
                )
            context["active_id"] = picking.id
        context["active_ids"] = self.ids
        context["active_model"] = "stock.picking"
        return {
            "name": _("Return Shipment"),
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "stock.return.picking",
            "target": "new",
            "context": context,
        }
