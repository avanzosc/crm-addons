# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class CrmClaimtype(models.Model):
    _inherit = "crm.claim.type"

    non_conformity = fields.Boolean(string="Is Non Conformity?", default=False)
