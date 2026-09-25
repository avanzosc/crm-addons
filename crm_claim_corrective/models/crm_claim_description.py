# Copyright 2021 Daniel Campos - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CrmClaimDescription(models.Model):
    _name = "crm.claim.description"
    _description = "Claim Description"

    name = fields.Char(required=True)
    description = fields.Text()
    type_description = fields.Selection(
        selection=[
            ("claim", "Claim Description"),
            ("cause", "Cause Description"),
            ("resolution", "Resolution Description"),
        ],
        string="Description Type",
    )
