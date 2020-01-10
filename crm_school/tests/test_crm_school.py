# Copyright 2019 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo.exceptions import ValidationError
from odoo.tests import common


@common.at_install(False)
@common.post_install(True)
class TestCrmSchool(common.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super(TestCrmSchool, cls).setUpClass()
        cls.partner_model = cls.env['res.partner']
        cls.wiz_model = cls.env['crm.lead2opportunity.partner']
        school_vals = {
            'name': 'School for test crm_school',
            'educational_category': 'school'}
        cls.school = cls.partner_model.create(school_vals)
        country_us = cls.env['res.country'].search(
            [('code', 'like', 'US')], limit=1)
        state = cls.env['res.country.state'].search(
            [('country_id', '=', country_us.id)], limit=1)
        cls.lead_model = cls.env['crm.lead']
        cls.lead_vals = {
            'name': 'Lead for test crm_school',
            'partner_name': 'Partner for test crm_school',
            'contact_name': 'Contact for test',
            'vat': 'X7413642Y',
            'street': 'aaaaa',
            'street2': 'bbbbb',
            'city': 'Azkoitia',
            'state_id': state.id,
            'zip': '20720',
            'country_id': country_us.id,
            'phone': '943943943',
            'mobile': '636636636',
            'email_from': 'test@avanzosc.es',
        }
        cls.family = cls.partner_model.create({
            'name': cls.lead_vals.get('partner_name'),
            'educational_category': 'family',
            'is_company': True,
        })
        cls.team = cls.env['crm.team'].create({
            'name': 'Test Team',
            'user_id': cls.env.ref('base.user_admin').id,
        })

    def test_crm_school(self):
        self.lead = self.lead_model.create(self.lead_vals)
        field_list = self.wiz_model.fields_get_keys()
        convert_vals = {
            'name': 'convert'}
        with self.assertRaises(ValidationError):
            self.wiz_model.with_context(
                active_id=self.lead.id).default_get(field_list)
        convert = self.wiz_model.create(convert_vals)
        with self.assertRaises(ValidationError):
            convert.with_context(active_ids=[self.lead.id]).action_apply()
        student_vals = {
            'name': 'Student for test crm_school',
            'birth_date': '2015-06-30',
            'gender': 'male',
            'school_id': self.school.id,
        }
        self.lead.write({
            'future_student_ids': [(0, 0, student_vals)],
            'team_id': self.team.id,
        })
        convert_vals = self.wiz_model.with_context(
            active_id=self.lead.id).default_get(field_list)
        convert = self.wiz_model.create(convert_vals)
        self.assertEqual(convert.user_id.id, self.uid)
        convert._onchange_team_id()
        self.assertNotEqual(self.team.user_id.id, self.uid)
        self.assertEqual(convert.user_id, self.team.user_id)
        self.assertEqual(
            self.lead.future_student_ids[:1].year_birth, 2015)
        convert.with_context(active_ids=[self.lead.id]).action_apply()
        student = self.lead.future_student_ids[:1].child_id
        self.assertTrue(student)
        self.assertEqual(
            self.lead.partner_id.educational_category, 'family')
        self.assertEqual(student.educational_category, 'otherchild')
        self.assertEqual(student.year_birth, 2015)
        self.assertIn(student.id, self.lead.allowed_student_ids.ids)
        new_student = self.lead.future_student_ids.new({
            'child_id': student,
        })
        self.assertFalse(new_student.name)
        new_student.onchange_child_id()
        self.assertEquals(new_student.child_id.name, new_student.name)

    def test_crm_school_partner(self):
        partner = self.family.copy()
        partner.write({
            'educational_category': 'progenitor',
            'is_company': False,
            'email': self.lead_vals.get('email_from'),
        })
        student_vals = {
            'name': 'Student for test crm_school',
            'birth_date': '2015-06-30',
            'gender': 'male',
            'school_id': self.school.id,
        }
        self.lead_vals.update({
            'partner_name': self.family.name,
            'future_student_ids': [(0, 0, student_vals)],
            'team_id': self.team.id,
        })
        self.lead = self.lead_model.create(self.lead_vals)
        field_list = self.wiz_model.fields_get_keys()
        convert_vals = self.wiz_model.with_context(
            active_id=self.lead.id, active_model=self.lead._name).default_get(
            field_list)
        self.assertEquals(self.family.id, convert_vals.get('partner_id'))
        self.family.write({
            'email': self.lead_vals.get('email_from'),
        })
        convert_vals = self.wiz_model.with_context(
            active_id=self.lead.id, active_model=self.lead._name).default_get(
            field_list)
        self.assertIn(self.family.id,
                      convert_vals.get('possible_partner_ids')[0][2])

    def test_crm_opportunity_blocked(self):
        with self.assertRaises(ValidationError):
            self.lead_model.with_context(default_type='opportunity').create(
                self.lead_vals)
