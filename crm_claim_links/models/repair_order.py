# Copyright 2014 Daniel Campos - AvanzOSC
# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class RepairOrder(models.Model):
    _inherit = "repair.order"

    claim_id = fields.Many2one(
        string="Claim", comodel_name="crm.claim", copy=False
    )
