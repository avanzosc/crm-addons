# Copyright 2025 Alfredo de la fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class CrmClaimReport(models.Model):
    _inherit = "crm.claim.report"

    department_id = fields.Many2one(
        string="Department", comodel_name="hr.department", readonly=True
    )

    @api.model
    def _select(self):
        select_str = super()._select()
        select_str += """
            , c.department_id as department_id
            """
        return select_str
