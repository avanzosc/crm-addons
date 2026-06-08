# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class AccountAnalyticLine(models.Model):
    _inherit = "account.analytic.line"

    claim_id = fields.Many2one(
        comodel_name="crm.claim",
        string="Claim",
        index=True,
    )
    task_id = fields.Many2one(
        comodel_name="project.task",
        string="Task",
        compute="_compute_task_id",
        store=True,
        readonly=False,
        index=True,
    )

    @api.depends("claim_id.task_id")
    def _compute_task_id(self):
        for line in self:
            if line.claim_id and not self.env.context.get("skip_task_id_compute"):
                line.task_id = line.claim_id.task_id
