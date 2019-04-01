# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models
from odoo.exceptions import Warning


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    user_input_ids = fields.One2many(
        comodel_name='survey.user_input', inverse_name='lead_id',
        string='Answers')
    user_input_count = fields.Integer(
        string='# Answers', compute='_compute_user_input_count')

    @api.depends('user_input_ids')
    def _compute_user_input_count(self):
        for record in self:
            record.user_input_count = len(record.user_input_ids)

    @api.multi
    def write(self, vals):
        stage_obj = self.env['crm.stage']
        user_input_obj = self.env['survey.user_input']
        if 'stage_id' in vals:
            stage = stage_obj.browse(vals.get('stage_id'))
            for record in self:
                if (record.stage_id.survey_id and
                        not record.user_input_ids.filtered(
                            lambda u: u.state == 'done' and
                                      u.survey_id ==
                                      record.stage_id.survey_id)):
                    raise Warning(_('Survey not answered.'))
                super(CrmLead, record).write(vals)
                if stage.survey_id:
                    user_input_obj.create({
                        'survey_id': stage.survey_id.id,
                        'lead_id': record.id,
                        'partner_id': record.partner_id.id,
                        'type': 'manually',
                    })
        return True

    @api.multi
    def action_start_survey(self):
        self.ensure_one()
        if not self.stage_id.survey_id:
            raise Warning(_('Stage has no survey.'))
        response_obj = self.env['survey.user_input']
        response = response_obj.search([
            ('lead_id', '=', self.id),
            ('survey_id', '=', self.stage_id.survey_id.id),
        ])
        # create a response and link it to this applicant
        if not response:
            response = self.env['survey.user_input'].create({
                'survey_id': self.stage_id.survey_id.id,
                'lead_id': self.id,
                'partner_id': self.partner_id.id,
            })
        # grab the token of the response and start surveying
        return self.stage_id.survey_id.with_context(
            survey_token=response.token).action_start_survey()

    @api.multi
    def action_open_response(self):
        self.ensure_one()
        action = self.env.ref('survey.action_survey_user_input')
        action_dict = action.read()[0]
        action_dict.update({
            'domain': [('lead_id', '=', self.id)],
        })
        return action_dict


class CrmStage(models.Model):
    _inherit = 'crm.stage'

    survey_id = fields.Many2one(
        comodel_name='survey.survey', string='Survey')
