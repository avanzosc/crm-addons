# Copyright 2019 Alfredo de la fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, fields, models


class CrmTeam(models.Model):
    _inherit = 'crm.team'

    school_id = fields.Many2one(
        comodel_name='res.partner', string='School',
        domain=[('educational_category', '=', 'school')])


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    future_student_ids = fields.One2many(
        comodel_name='crm.lead.future.student', inverse_name='crm_lead_id',
        string='Future students')

    @api.multi
    def _create_lead_partner(self):
        partner = super(CrmLead, self)._create_lead_partner()
        partner.educational_category = 'family'
        return partner

    @api.multi
    def convert_opportunity(self, partner_id, user_ids=False, team_id=False):
        res = super(CrmLead, self).convert_opportunity(
            partner_id, user_ids=user_ids, team_id=team_id)
        for lead in self:
            for future_student in lead.future_student_ids.filtered(
                    lambda c: not c.child_id):
                new_student = self.env['res.partner'].create(
                    self.catch_new_student_vals(future_student))
                future_student.child_id = new_student.id
        return res

    def catch_new_student_vals(self, future_student):
        vals = {
            'name': future_student.name,
            'birthdate_date': future_student.birth_date,
            'gender': future_student.gender,
            'educational_category': 'other',
            # 'year_birth': future_student.year_birth
        }
        if self.partner_id.street:
            vals['street'] = self.partner_id.street
        if self.partner_id.street2:
            vals['street2'] = self.partner_id.street2
        if self.partner_id.city:
            vals['city'] = self.partner_id.city
        if self.partner_id.state_id:
            vals['state_id'] = self.partner_id.state_id.id
        if self.partner_id.zip:
            vals['zip'] = self.partner_id.zip
        if self.partner_id.country_id:
            vals['country_id'] = self.partner_id.country_id.id
        if self.partner_id.phone:
            vals['phone'] = self.partner_id.phone
        if self.partner_id.mobile:
            vals['mobile'] = self.partner_id.mobile
        if self.partner_id.email:
            vals['email'] = self.partner_id.email
        return vals


class CrmLeadFutureStudent(models.Model):
    _name = 'crm.lead.future.student'
    _description = 'Future student from leads'

    @api.model
    def _get_selection_gender(self):
        return self.env['res.partner'].fields_get(
            allfields=['gender'])['gender']['selection']

    crm_lead_id = fields.Many2one(
        comodel_name="crm.lead", string='Lead', required=True)
    child_id = fields.Many2one(
        comodel_name='res.partner', string='Child',
        domain=[('educational_category', 'in', ('student', 'other'))])
    name = fields.Char(string='Child name')
    birth_date = fields.Date(string='Birth date')
    year_birth = fields.Integer(
        string='Year of birth', compute='_compute_year_birth')
    course_id = fields.Many2one(
        comodel_name='education.course', string='Initial school course')
    gender = fields.Selection(
        string='Gender', selection=_get_selection_gender)
    school_id = fields.Many2one(
        comodel_name='res.partner', string='School',
        domain=[('educational_category', '=', 'school')])
    academic_year_id = fields.Many2one(
        comodel_name='education.academic_year', string='Academic year')

    @api.onchange('child_id')
    def onchange_child_id(self):
        if self.child_id:
            self.name = self.child_id.name
            self.birth_date = self.child_id.birthdate_date
            self.gender = self.child_id.gender

    @api.multi
    def _compute_year_birth(self):
        for student in self.filtered(lambda c: c.birth_date):
            birth_date = fields.Date.from_string(student.birth_date)
            student.year_birth = birth_date.year
