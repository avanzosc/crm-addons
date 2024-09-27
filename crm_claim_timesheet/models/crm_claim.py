# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


from odoo import fields, models


class CrmClaim(models.Model):
    _inherit = 'crm.claim'

    project_id = fields.Many2one(
        comodel_name='project.project',
        string="Project",
    )
    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        inverse_name='claim_id',
        string="Timesheet",
    )
