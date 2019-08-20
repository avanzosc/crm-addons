# Copyright 2019 Alfredo de la fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields, api


class CrmClaimCategory(models.Model):
    _inherit = 'crm.claim.category'

    mail_server_id = fields.Many2one(
        string='Mail server', comodel_name='fetchmail.server')


class CrmClaim(models.Model):
    _inherit = 'crm.claim'

    team_users_ids = fields.Many2many(
        string='Team users', comodel_name='res.users',
        relation='rel_claim_team_users', column1='claim_id',
        column2='user_id', compute='_compute_team_users_ids', store=True)

    @api.depends('team_id', 'team_id.member_ids')
    def _compute_team_users_ids(self):
        for claim in self:
            if (not claim.team_id or
               (claim.team_id and not claim.team_id.member_ids)):
                claim.team_users_ids = [(6, 0, [])]
            if claim.team_id and claim.team_id.member_ids:
                users = claim.team_id.mapped('member_ids.id')
                claim.team_users_ids = [(6, 0, users)]

    @api.onchange('categ_id')
    def onchange_categ_id(self):
        res = super(CrmClaim, self).onchange_categ_id()
        if self.team_id and self.team_id.user_id:
            self.user_id = self.team_id.user_id.id
        return res

    @api.model
    def create(self, values):
        server_obj = self.env['fetchmail.server']
        if (self.env.context.get('server_type', False) and
            self.env.context.get('server_type') == 'imap' and
                self.env.context.get('fetchmail_server_id', False)):
            server = server_obj.browse(
                self.env.context.get('fetchmail_server_id'))
            if len(server.claim_category_ids) == 1:
                values['categ_id'] = server.claim_category_ids[0].id
                if server.claim_category_ids[0].team_id:
                    values['team_id'] = server.claim_category_ids[0].team_id.id
                    if server.claim_category_ids[0].team_id.user_id:
                        values['user_id'] = (
                            server.claim_category_ids[0].team_id.user_id.id)
        return super(CrmClaim, self).create(values)
