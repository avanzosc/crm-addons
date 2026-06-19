# Copyright 2021 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class RepairOrder(models.Model):
    _inherit = 'repair.order'

    claim_id = fields.Many2one(
        string='Claim', comodel_name='crm.claim')
