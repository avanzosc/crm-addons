# Copyright 2025 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    mrp_production_control_ids = fields.One2many(
        string="Production Controls",
        comodel_name="mrp.production.control",
        inverse_name="claim_id",
        copy=False,
    )
    count_mrp_production_control = fields.Integer(
        string="Production Controls Counter",
        compute="_compute_count_mrp_production_control",
    )

    def _compute_count_mrp_production_control(self):
        for claim in self:
            claim.count_mrp_production_control = len(claim.mrp_production_control_ids)

    def action_view_mrp_production_control(self):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "mrp_production_control.action_production_control_records"
        )
        action["domain"] = [("id", "in", self.mrp_production_control_ids.ids)]
        return action
