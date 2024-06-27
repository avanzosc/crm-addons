# Copyright 2022 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    sign = fields.Binary(string="Signature")
