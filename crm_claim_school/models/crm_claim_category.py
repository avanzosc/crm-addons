# Copyright 2019 Alfredo de la fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class CrmClaimCategory(models.Model):
    _inherit = 'crm.claim.category'

    mail_server_id = fields.Many2one(
        string='Mail server', comodel_name='fetchmail.server')
