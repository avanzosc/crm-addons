# Copyright 2022 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    contact_type_id = fields.Many2one(
        string="Contact type",
        comodel_name="res.partner.type",
    )
