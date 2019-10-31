# Copyright 2019 Alfredo de la fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class FetchmailServer(models.Model):
    _inherit = 'fetchmail.server'

    school_id = fields.Many2one(
        string='School', comodel_name='res.partner',
        domain=[('educational_category', '=', 'school')])
    claim_category_ids = fields.One2many(
        string='Claims categories', comodel_name='crm.claim.category',
        inverse_name='mail_server_id')
