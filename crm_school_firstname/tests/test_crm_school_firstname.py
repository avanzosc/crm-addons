# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import common


@common.at_install(False)
@common.post_install(True)
class TestCrmSchoolFirstname(common.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super(TestCrmSchoolFirstname, cls).setUpClass()
        cls.lead_model = cls.env['crm.lead']
        cls.wiz_model = cls.env['crm.lead2opportunity.partner']
        cls.lastname = 'Family Name'
        cls.student_name = 'Student Name'
        cls.lead = cls.lead_model.create({
            'name': cls.lastname,
            'partner_name': cls.lastname,
            'contact_name': 'Contact Name',
            'contact_lastname': cls.lastname,
            'future_student_ids': [(0, 0, {
                'name': cls.student_name,
                'lastname': cls.lastname,
            })],
        })
        cls.partner = cls.env['res.partner'].create({
            'name': cls.lastname,
            'educational_category': 'family',
        })
        cls.student = cls.env['res.partner'].create({
            'firstname': cls.student_name,
            'lastname': cls.lastname,
            'parent_id': cls.partner.id,
        })

    def test_crm_school_first_name(self):
        for student in self.lead.future_student_ids:
            self.assertFalse(student.child_id)
        contact = self.lead._create_lead_partner()
        self.lead.convert_opportunity(contact.commercial_partner_id.id)
        for student in self.lead.future_student_ids:
            self.assertTrue(student.child_id)
            child = student.child_id
        new_student = self.lead.future_student_ids.new({'child_id': child.id})
        new_student.onchange_child_id()
        self.assertEqual(new_student.name, new_student.child_id.firstname)
        self.assertEqual(new_student.lastname, new_student.child_id.lastname)

    def test_crm_school_first_name_nocontact(self):
        self.lead.write({
            'contact_name': False,
            'contact_lastname': False,
        })
        for student in self.lead.future_student_ids:
            self.assertFalse(student.child_id)
        contact = self.lead._create_lead_partner()
        self.lead.convert_opportunity(contact.commercial_partner_id.id)
        for student in self.lead.future_student_ids:
            self.assertTrue(student.child_id)
            child = student.child_id
        new_student = self.lead.future_student_ids.new({'child_id': child.id})
        new_student.onchange_child_id()
        self.assertEqual(new_student.name, new_student.child_id.firstname)
        self.assertEqual(new_student.lastname, new_student.child_id.lastname)

    def test_crm_school_wizard(self):
        field_list = self.wiz_model.fields_get_keys()
        convert_vals = self.wiz_model.with_context(
            active_id=self.lead.id).default_get(field_list)
        self.assertIn(self.partner.id, convert_vals.get(
            'possible_partner_ids')[0][2])
