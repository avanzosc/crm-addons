# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.addons.crm.tests import common
from odoo.exceptions import UserError, Warning


class TestCrmSurvey(common.TestCrmCases):

    def setUp(self):
        super(TestCrmSurvey, self).setUp()
        self.stage1 = self.env.ref('crm.stage_lead1')
        self.stage2 = self.env.ref('crm.stage_lead2')
        self.opportunity = self.env['crm.lead'].search([
            ('stage_id', '=', self.stage1.id),
            ('type', '=', 'opportunity')
        ], limit=1) or self.env.ref('crm.crm_case_13')
        self.survey_id = self.ref('survey.feedback_form')

    def test_change_stage(self):
        self.stage1.write({
            'survey_id': self.survey_id,
        })
        self.assertFalse(self.opportunity.user_input_ids)
        self.assertFalse(self.opportunity.user_input_count)
        with self.assertRaises(UserError):
            self.opportunity.write({
                'stage_id': self.stage2.id,
            })
        action_dict = self.opportunity.action_start_survey()
        self.assertEquals(action_dict.get('type'), 'ir.actions.act_url')
        self.assertEquals(self.opportunity.user_input_count, 1)
        action_dict = self.opportunity.action_open_response()
        self.assertEquals(action_dict.get('domain'),
                          [('lead_id', '=', self.opportunity.id)])
        with self.assertRaises(UserError):
            self.opportunity.write({
                'stage_id': self.stage2.id,
            })
        self.opportunity.user_input_ids.write({
            'state': 'done',
        })
        self.opportunity.write({
            'stage_id': self.stage2.id,
        })

    def test_create_response(self):
        self.stage2.write({
            'survey_id': self.survey_id,
        })
        self.assertFalse(self.opportunity.user_input_ids)
        self.assertFalse(self.opportunity.user_input_count)
        with self.assertRaises(Warning):
            self.opportunity.action_start_survey()
        self.opportunity.write({
            'stage_id': self.stage2.id,
        })
        self.assertEquals(self.opportunity.user_input_count, 1)
