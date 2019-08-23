# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    permission_ids = fields.Many2many(
        comodel_name='res.partner.permission', string='Permissions',
        compute='_compute_permission_ids', store=True,
        column1='lead_id', column2='permission_id',
        relation='rel_lead_permission')

    @api.depends('future_student_ids', 'future_student_ids.child_id',
                 'future_student_ids.child_id.permission_ids')
    def _compute_permission_ids(self):
        for claim in self:
            claim.permission_ids = claim.mapped(
                'future_student_ids.child_id.permission_ids')
