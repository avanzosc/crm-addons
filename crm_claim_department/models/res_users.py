# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models


class ResUsers(models.Model):
    _inherit = "res.users"

    def _search_user_department(self):
        if self.employee_id and self.employee_id.department_id:
            return self.employee_id.department_id.id
        else:
            return self.env["hr.department"]
