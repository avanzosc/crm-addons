# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import common
from odoo.addons.crm_school.tests.test_crm_school import \
    TestCrmSchool


@common.at_install(False)
@common.post_install(True)
class TestCrmSchoolPermission(TestCrmSchool):

    @classmethod
    def setUpClass(cls):
        super(TestCrmSchoolPermission, cls).setUpClass()
        cls.permission_model = cls.env['res.partner.permission']
        cls.permission_type = cls.env['res.partner.permission.type'].create({
            'name': 'Test Type',
            'admission_default': True,
        })

    def test_crm_school_permission(self):
        student_vals = {
            'name': 'Student for test crm_school',
            'birth_date': '2015-06-30',
            'gender': 'male',
            'school_id': self.school.id,
        }
        self.lead_vals.update({
            'partner_id': self.family.id,
            'future_student_ids': [(0, 0, student_vals)],
            'team_id': self.team.id,
        })
        self.lead = self.lead_model.create(self.lead_vals)
        self.assertFalse(self.lead.permission_ids)
        field_list = self.wiz_model.fields_get_keys()
        convert_vals = self.wiz_model.with_context(
            active_id=self.lead.id).default_get(field_list)
        convert = self.wiz_model.create(convert_vals)
        convert.with_context(active_ids=[self.lead.id]).action_apply()
        self.assertTrue(self.lead.permission_ids)

    def test_crm_school(self):
        """Don't repeat this test."""
        pass

    def test_crm_school_partner(self):
        """Don't repeat this test."""
        pass

    def test_crm_opportunity_blocked(self):
        """Don't repeat this test."""
        pass
