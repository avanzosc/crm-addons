# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CrmClaimStage(models.Model):
    _inherit = "crm.claim.stage"

    closed = fields.Boolean()
