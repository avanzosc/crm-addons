# Copyright 2026 Lucía Echeverría - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CrmClaimTaskWizard(models.TransientModel):
    _name = "crm.claim.task.wizard"
    _description = "Change Claim Task"

    claim_id = fields.Many2one(
        comodel_name="crm.claim",
        required=True,
        readonly=True,
    )
    project_id = fields.Many2one(
        comodel_name="project.project",
        related="claim_id.project_id",
        readonly=True,
    )
    current_task_id = fields.Many2one(
        comodel_name="project.task",
        related="claim_id.task_id",
        readonly=True,
    )
    new_task_id = fields.Many2one(
        comodel_name="project.task",
        required=True,
    )

    def action_update_timesheets(self):
        self.claim_id.write({"task_id": self.new_task_id.id})
        return {"type": "ir.actions.act_window_close"}

    def action_no_update(self):
        self.claim_id.with_context(skip_task_id_compute=True).write(
            {"task_id": self.new_task_id.id}
        )
        return {"type": "ir.actions.act_window_close"}
