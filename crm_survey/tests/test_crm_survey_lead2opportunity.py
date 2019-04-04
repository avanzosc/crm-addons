# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.addons.crm.tests.test_lead2opportunity import \
    TestLead2opportunity2win
from odoo.exceptions import UserError


class TestCrmSurveyLead2Opportunity(TestLead2opportunity2win):
    def test_lead2opportunity2win(self):
        default_stage = self.env.ref("crm.stage_lead1")
        default_stage.survey_id = self.env.ref('survey.feedback_form')
        with self.assertRaises(UserError):
            super(TestCrmSurveyLead2Opportunity,
                  self).test_lead2opportunity2win()
