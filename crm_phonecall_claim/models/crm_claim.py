# Copyright 2021 Berezi - Iker - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import _, fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    def _compute_count_phonecall(self):
        for claim in self:
            claim.count_phonecall = len(claim.phonecall_ids)

    def _compute_phonecall_ids(self):
        for claim in self:
            cond = [
                "|",
                ("id", "=", claim.phonecall_id.id),
                ("claim_id", "=", claim.id),
            ]
            calls = self.env["crm.phonecall"].search(cond)
            claim.phonecall_ids = [(6, 0, calls.ids)]

    phonecall_ids = fields.Many2many(
        string="Phone calls",
        comodel_name="crm.phonecall",
        compute="_compute_phonecall_ids",
    )
    count_phonecall = fields.Integer(
        string="# Phone calls",
        compute="_compute_count_phonecall",
    )
    phonecall_id = fields.Many2one(
        string="Phone call",
        comodel_name="crm.phonecall",
    )

    def action_view_phonecall(self):
        context = self.env.context.copy()
        context.update(
            {
                "default_claim_id": self.id,
            }
        )
        if self.partner_id:
            context.update(
                {
                    "default_partner_id": self.partner_id.id,
                }
            )
        return {
            "name": _("Phone calls"),
            "view_mode": "tree,form",
            "res_model": "crm.phonecall",
            "views": [
                [self.env.ref("crm_phonecall.crm_case_phone_tree_view").id, "tree"],
                [False, "form"],
            ],
            "domain": [("id", "in", self.phonecall_ids.ids)],
            "type": "ir.actions.act_window",
            "context": context,
        }
