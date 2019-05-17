# Copyright 2019 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestCrmSchool(TransactionCase):

    def setUp(self):
        super(TestCrmSchool, self).setUp()
        self.partner_model = self.env['res.partner']
        self.wiz_model = self.env['crm.lead2opportunity.partner']
        school_vals = {
            'name': 'School for test crm_school',
            'educational_category': 'school'}
        self.school = self.partner_model.create(school_vals)
        country_us = self.env['res.country'].search(
            [('code', 'like', 'US')], limit=1)
        state = self.env['res.country.state'].search(
            [('country_id', '=', country_us.id)], limit=1)
        self.lead_model = self.env['crm.lead']
        self.lead_vals = {
            'name': 'Lead for test crm_school',
            'partner_name': 'Partner for test crm_school',
            'contact_name': 'Contact for test',
            'street': 'aaaaa',
            'street2': 'bbbbb',
            'city': 'Azkotitia',
            'state_id': state.id,
            'zip': '20720',
            'country_id': country_us.id,
            'phone': '943943943',
            'mobile': '636636636',
            'email_from': 'test@avanzosc.es',
        }

    def test_crm_school(self):
        self.lead = self.lead_model.create(self.lead_vals)
        field_list = ['name', 'user_id', 'team_id', 'action']
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
        })
        self.assertEqual(
            self.lead.future_student_ids[:1].year_birth, 2015)
        convert.with_context(active_ids=[self.lead.id]).action_apply()
        student = self.lead.future_student_ids[:1].child_id
        self.assertTrue(student)
        self.assertEqual(
            self.lead.partner_id.educational_category, 'family')
        self.assertEqual(
            self.lead.partner_id.commercial_partner_id.educational_category,
            'progenitor')
        self.assertEqual(student.educational_category, 'other')
        self.assertEqual(student.year_birth, 2015)
        self.assertIn(student.id, self.lead.allowed_student_ids.ids)

    def test_crm_opportunity_blocked(self):
        with self.assertRaises(ValidationError):
            self.lead_model.with_context(default_type='opportunity').create(
                self.lead_vals)
