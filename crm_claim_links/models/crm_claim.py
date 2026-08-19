# Copyright 2014 Daniel Campos - AvanzOSC
# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import _, api, fields, models
from odoo.models import expression
from odoo.tools.safe_eval import safe_eval


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    picking_ids = fields.One2many(
        string="Stock Pickings",
        comodel_name="stock.picking",
        inverse_name="claim_id",
        copy=False,
    )
    repair_ids = fields.One2many(
        string="Repair Orders",
        comodel_name="repair.order",
        inverse_name="claim_id",
        copy=False,
    )
    pickings_count = fields.Integer(
        string="Num. Pickings", compute="_compute_pickings_count"
    )
    repairs_count = fields.Integer(
        string="Num. Repairs", compute="_compute_repairs_count"
    )

    def _compute_pickings_count(self):
        for claim in self:
            claim.pickings_count = len(claim.picking_ids)

    def _compute_repairs_count(self):
        for claim in self:
            claim.repairs_count = len(claim.repair_ids)

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        args = args or []
        if name:
            args = expression.AND(
                [
                    args,
                    expression.OR(
                        [
                            [("name", operator, name)],
                            [("code", operator, name)],
                        ]
                    ),
                ]
            )
        return super().name_search(
            name="",
            args=args,
            operator=operator,
            limit=limit,
        )

    @api.depends("name", "code")
    def _compute_display_name(self):
        for claim in self:
            display_name = claim.name
            if claim.code:
                display_name = f"[{claim.code}] {display_name}"
            claim.display_name = display_name

    def action_view_pickings(self):
        self.ensure_one()
        context = self.env.context.copy()
        context.update(
            {
                "default_sale_type": self.id,
            }
        )
        return {
            "name": _("Pickings"),
            "view_mode": "list,form",
            #            "view_id": self.env.ref(
            #                "custom_sale_order_type_route.view_partner_tree_editable"
            #            ).id,
            "res_model": "stock.picking",
            "domain": [("claim_id", "=", self.id)],
            "type": "ir.actions.act_window",
            "context": context,
        }

    def action_view_repairs(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id(
            "repair.action_repair_order_tree"
        )
        action["domain"] = expression.AND(
            [
                [("claim_id", "=", self.id)],
                safe_eval(action.get("domain") or "[]"),
            ]
        )
        return action
