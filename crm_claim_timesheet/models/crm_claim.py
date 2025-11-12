# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    project_id = fields.Many2one(
        comodel_name="project.project",
        string="Project",
        index=True,
    )
    task_id = fields.Many2one(
        comodel_name="project.task",
        string="Task",
        index=True,
    )
    timesheet_ids = fields.One2many(
        comodel_name="account.analytic.line",
        inverse_name="claim_id",
        string="Timesheet",
    )
    planned_hours = fields.Float(
        string="Initially Planned Hours",
        help="Time planned to achieve this claim.",
        tracking=True,
    )
    remaining_hours = fields.Float(
        compute="_compute_remaining_hours",
        store=True,
        readonly=True,
        help="Total remaining time, can be re-estimated periodically by the "
        "assignee of the claim.",
    )
    effective_hours = fields.Float(
        string="Hours Spent",
        compute="_compute_effective_hours",
        compute_sudo=True,
        store=True,
        help="Time spent on this claim.",
    )
    task_remaining_hours = fields.Float(
        string="Task Remaining Hours",
        related="task_id.remaining_hours",
        readonly=True,
    )

    @api.depends("timesheet_ids.unit_amount")
    def _compute_effective_hours(self):
        for claim in self:
            claim.effective_hours = round(
                sum(claim.timesheet_ids.mapped("unit_amount")), 2
            )

    @api.depends("effective_hours", "planned_hours")
    def _compute_remaining_hours(self):
        for claim in self:
            claim.remaining_hours = claim.planned_hours - claim.effective_hours

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        res = super().onchange_partner_id()
        projects = self.env["project.project"].search(
            [("partner_id", "=", self.commercial_partner_id.id)]
        )
        if len(projects) == 1:
            self.project_id = projects[:1]
        return res

    @api.onchange("project_id")
    def _onchange_project_id(self):
        self.task_id = (
            self.project_id.task_ids[:1]
            if len(self.project_id.task_ids) == 1
            else False
        )

    @api.model
    def message_new(self, msg, custom_values=None):
        """Overrides mail_thread message_new that is called by the mailgateway
        through message_process.
        This override updates the document according to the email.
        """
        if custom_values is None:
            custom_values = {}
        partner_id = msg.get("author_id", False)
        defaults = {}
        if partner_id:
            partner = self.env["res.partner"].browse(partner_id)
            tasks = self.env["project.task"].search(
                [
                    ("project_id.partner_id", "=", partner.commercial_partner_id.id),
                    "|",
                    ("stage_id", "=", False),
                    ("stage_id.is_closed", "=", False),
                ]
            )
            if len(tasks) == 1:
                defaults.update(
                    {
                        "task_id": tasks[:1].id,
                        "project_id": tasks[:1].project_id.id,
                    }
                )
            else:
                projects = tasks.mapped("project_id")
                if len(projects) == 1:
                    defaults.update(
                        {
                            "project_id": projects[:1].id,
                        }
                    )
        defaults.update(custom_values)
        return super().message_new(msg, custom_values=defaults)
