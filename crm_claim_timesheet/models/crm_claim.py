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
        string="Remaining Hours",
        compute="_compute_remaining_hours",
        store=True,
        readonly=True,
        help="Total remaining time, can be re-estimated periodically by the "
             "assignee of the claim.")
    effective_hours = fields.Float(
        string="Hours Spent",
        compute="_compute_effective_hours",
        compute_sudo=True,
        store=True,
        help="Time spent on this claim.")

    @api.depends('timesheet_ids.unit_amount')
    def _compute_effective_hours(self):
        for claim in self:
            claim.effective_hours = round(
                sum(claim.timesheet_ids.mapped('unit_amount')), 2)

    @api.depends('effective_hours', 'planned_hours')
    def _compute_remaining_hours(self):
        for claim in self:
            claim.remaining_hours = claim.planned_hours - claim.effective_hours
