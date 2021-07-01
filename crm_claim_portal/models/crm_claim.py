# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models


class CrmClaim(models.Model):
    _name = "crm.claim"
    _inherit = ["crm.claim", "portal.mixin", "rating.mixin"]
