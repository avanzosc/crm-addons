# Copyright 2025 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class MrpProductionControl(models.Model):
    _inherit = "mrp.production.control"

    claim_id = fields.Many2one(string="Claim", comodel_name="crm.claim", copy=False)
