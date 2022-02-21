# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    claim_id = fields.Many2one(
        comodel_name='crm.claim',
        string='Claim',
    )

    @api.onchange('claim_id')
    def _onchange_claim_id(self):
        if self.claim_id.project_id:
            self.project_id = self.claim_id.project_id
