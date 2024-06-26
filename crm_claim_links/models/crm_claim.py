# Copyright 2014 Daniel Campos - AvanzOSC
# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    picking_ids = fields.One2many(
        string="Stock Pickings",
        comodel_name="stock.picking",
        inverse_name="claim_id",
        copy=False,
    )
    repair_ids = fields.One2many(
        string="Repair Orders",
        comodel_name="repair.order",
        inverse_name="claim_id",
        copy=False,
    )
