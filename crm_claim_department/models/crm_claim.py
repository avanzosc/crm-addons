# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    def _default_department_id(self):
        return self.env.user._search_user_department()

    department_id = fields.Many2one(
        string="Department",
        comodel_name="hr.department",
        default=_default_department_id,
    )

    @api.onchange("user_id")
    def onchange_user_id(self):
        self.department_id = (
            self.user_id._search_user_department()
            if self.user_id
            else self.env["hr.department"]
        )
