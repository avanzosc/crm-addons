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
        for lead in self:
            permissions = self.env["res.partner.permission"]
            for future_student in lead.future_student_ids:
                partner_permissions = future_student.child_id.permission_ids
                permissions |= partner_permissions.filtered(
                    lambda p: p.center_id == future_student.school_id)
            lead.permission_ids = [(6, 0, permissions.ids)]

    def catch_new_student_vals(self, future_student):
        res = super(CrmLead, self).catch_new_student_vals(future_student)
        types = self.env['res.partner.permission.type'].search([(
            'admission_default', '=', True)])
        res.update({
            'permission_ids': [
                (0, 0, {
                    'type_id': x.id,
                    'center_id': future_student.school_id.id,
                }) for x in types],
        })
        return res

    @api.multi
    def convert_opportunity(self, partner_id, user_ids=False, team_id=False):
        result = super(CrmLead, self).convert_opportunity(
            partner_id, user_ids=user_ids, team_id=team_id)
        permission_obj = self.env["res.partner.permission"]
        types = self.env['res.partner.permission.type'].search([(
            'admission_default', '=', True)])
        for student in self.mapped("future_student_ids").filtered("child_id"):
            for permission_type in types:
                permission_obj.find_or_create_permission(
                    student.child_id, student.school_id, permission_type)
        return result
