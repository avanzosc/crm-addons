# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    claim_count = fields.Integer(
        string="# Claims",
        compute="_compute_claim_count",
    )
    claim_ids = fields.One2many(
        comodel_name="crm.claim",
        inverse_name="task_id",
        string="Claims",
    )

    @api.depends("claim_ids")
    def _compute_claim_count(self):
        for task in self:
            task.claim_count = len(task.claim_ids)
