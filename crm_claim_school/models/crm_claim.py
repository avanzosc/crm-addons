# Copyright 2019 Alfredo de la fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, fields, models


class CrmClaim(models.Model):
    _inherit = 'crm.claim'

    team_users_ids = fields.Many2many(
        string='Team users', comodel_name='res.users',
        relation='rel_claim_team_users', column1='claim_id',
        column2='user_id', compute='_compute_team_users_ids', store=True)

    @api.multi
    @api.depends('team_id', 'team_id.member_ids')
    def _compute_team_users_ids(self):
        for claim in self:
            claim.team_users_ids = [
                (6, 0, claim.mapped('team_id.member_ids').ids)]

    @api.onchange('categ_id')
    def onchange_categ_id(self):
        res = super(CrmClaim, self).onchange_categ_id()
        if self.team_id and self.team_id.user_id:
            self.user_id = self.team_id.user_id
        return res

    @api.model
    def create(self, values):
        mail_server = self.env['fetchmail.server'].browse(
            self.env.context.get('fetchmail_server_id', False))
        if mail_server and len(mail_server.claim_category_ids) == 1:
            category = mail_server.claim_category_ids[:1]
            values.update({
                'categ_id': category.id,
                'team_id': category.team_id.id if category.team_id else
                values.get('team_id'),
                'user_id': category.team_id.user_id.id if
                category.team_id.user_id else
                values.get('user_id'),
            })
        return super(CrmClaim, self).create(values)
