# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    extra_category_id = fields.Many2one(
        string="Extra Category", comodel_name="crm.claim.category",
        copy=False
    )