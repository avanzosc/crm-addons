# Copyright 2019 Alfredo de la fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


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
    educational_category = fields.Selection(
        string='Educational category',
        related='partner_id.educational_category')
    family_ids = fields.One2many(
        comodel_name='res.partner.family', inverse_name='family_id',
        string='Families', related='partner_id.family_ids')

    @api.model
    def create(self, values):
        if (values.get('type') == 'opportunity' or
                ('type' not in values and self.env.context.get(
                    'default_type') == 'opportunity')):
            raise ValidationError(
                _('You aren\'t allowed to create opportunities, you must '
                  'start from lead'))
        return super(CrmLead, self).create(values)

    @api.multi
    def _create_lead_partner_data(self, name, is_company, parent_id=False):
        partner_dict = super(CrmLead, self)._create_lead_partner_data(
            name, is_company, parent_id=parent_id)
        partner_dict.update({
            'educational_category': 'family' if is_company else 'progenitor',
        })
        return partner_dict

    @api.multi
    def convert_opportunity(self, partner_id, user_ids=False, team_id=False):
        partner_model = self.env['res.partner']
        family_model = self.env['res.partner.family']
        res = super(CrmLead, self).convert_opportunity(
            partner_id, user_ids=user_ids, team_id=team_id)
        for lead in self:
            for future_student in lead.future_student_ids.filtered(
                    lambda c: not c.child_id):
                new_student = partner_model.create(
                    self.catch_new_student_vals(future_student))
                future_student.child_id = new_student
                family_model.create({
                    'child2_id': new_student.id,
                    'responsible_id': lead.partner_id.id,
                    'family_id': lead.partner_id.commercial_partner_id.id,
                    'relation': 'progenitor',
                })
        return res

    def catch_new_student_vals(self, future_student):
        partner_dict = self._create_lead_partner_data(
            future_student.name, False,
            parent_id=self.partner_id.commercial_partner_id.id)
        partner_dict.update({
            'birthdate_date': future_student.birth_date,
            'gender': future_student.gender,
            'educational_category': 'other',
        })
        return partner_dict


class CrmLeadFutureStudent(models.Model):
    _name = 'crm.lead.future.student'
    _description = 'Future student from leads'

    @api.model
    def _get_selection_gender(self):
        return self.env['res.partner'].fields_get(
            allfields=['gender'])['gender']['selection']

    crm_lead_id = fields.Many2one(
        comodel_name="crm.lead", string='Lead', required=True,
        ondelete='cascade')
    child_id = fields.Many2one(
        comodel_name='res.partner', string='Child',
        domain=[('educational_category', 'in', ('student', 'other'))])
    name = fields.Char(string='Child name', required=True)
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
        comodel_name='education.academic_year', string='Academic year',
        domain=lambda s: [('date_end', '>', fields.Date.context_today(s))])

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
