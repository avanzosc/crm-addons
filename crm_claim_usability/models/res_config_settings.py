# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_crm_claim_technical = fields.Boolean(
        string="Show Metadata Info in Claims",
        implied_group="crm_claim_usability.group_crm_claim_technical",
    )
