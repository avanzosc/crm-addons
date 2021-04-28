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
    name = fields.Char(required=False)
    allowed_student_ids = fields.Many2many(
        comodel_name='res.partner', compute='_compute_allowed_student_ids')
    payer_ids = fields.One2many(
        comodel_name='res.partner.family', inverse_name='crm_lead_id',
        string='Payers')

    @api.depends('future_student_ids', 'future_student_ids.child_id')
    def _compute_allowed_student_ids(self):
        for lead in self.filtered(lambda c: c.future_student_ids):
            students = lead.mapped('future_student_ids.child_id')
            if students:
                lead.allowed_student_ids = [(6, 0, students.ids)]

    @api.model
    def create(self, values):
        if (values.get('type') == 'opportunity' or
                ('type' not in values and self.env.context.get(
                    'default_type') == 'opportunity')):
            raise ValidationError(
                _('You aren\'t allowed to create opportunities, you must '
                  'start from lead'))
        if not values.get("name"):
            values.update({
                "name": values.get("partner_name"),
            })
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
                if partner_id != lead.partner_id.id:
                    family_model.create({
                        'crm_lead_id': lead.id,
                        'child2_id': new_student.id,
                        'responsible_id': partner_id,
                        'family_id': lead.partner_id.id,
                        'relation': 'progenitor',
                    })
                progenitors = lead.partner_id.family_progenitor_ids.filtered(
                    lambda p: p.id != partner_id)
                for progenitor in progenitors:
                    family_model.create({
                        'crm_lead_id': lead.id,
                        'child2_id': new_student.id,
                        'responsible_id': progenitor.id,
                        'family_id': lead.partner_id.id,
                        'relation': 'progenitor',
                    })
        return res

    @api.multi
    def merge_opportunity(self, user_id=False, team_id=False):
        partner_model = self.env['res.partner']
        family_model = self.env['res.partner.family']
        lead = super(CrmLead, self).merge_opportunity(
            user_id=user_id, team_id=team_id)
        for future_student in lead.future_student_ids.filtered(
                lambda c: not c.child_id):
            new_student = partner_model.create(
                lead.catch_new_student_vals(future_student))
            future_student.child_id = new_student
            for progenitor in lead.partner_id.family_progenitor_ids:
                family_model.create({
                    'crm_lead_id': lead.id,
                    'child2_id': new_student.id,
                    'responsible_id': progenitor.id,
                    'family_id': lead.partner_id.id,
                    'relation': 'progenitor',
                })
        return lead

    def catch_new_student_vals(self, future_student):
        partner_dict = self._create_lead_partner_data(
            future_student.name, False,
            parent_id=self.partner_id.id)
        partner_dict.update({
            'birthdate_date': future_student.birth_date,
            'gender': future_student.gender,
            'educational_category': 'otherchild',
        })
        return partner_dict

    @api.multi
    def _convert_opportunity_data(self, customer, team_id=False):
        res = super(CrmLead, self)._convert_opportunity_data(
            customer, team_id=team_id)
        if customer and customer.parent_id:
            res['partner_id'] = customer.parent_id.id
        return res

    @api.multi
    def _merge_future_students(self, opportunities):
        self.ensure_one()
        opportunities.future_student_ids.write({
            "crm_lead_id": self.id,
        })
        return True

    @api.multi
    def merge_dependences(self, opportunities):
        self.ensure_one()
        super(CrmLead, self).merge_dependences(opportunities)
        self._merge_future_students(opportunities)


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
        domain=[('educational_category', 'in', ('student', 'otherchild'))])
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
    lead_stage_id = fields.Many2one(
        comodel_name="crm.stage", string="Stage",
        related="crm_lead_id.stage_id", store=True)

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
