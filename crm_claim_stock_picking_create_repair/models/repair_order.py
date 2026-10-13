# Copyright 2026 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class RepairOrder(models.Model):
    _inherit = "repair.order"

    crm_claim_id = fields.Many2one(string="Claim", comodel_name="crm.claim")

    def _catch_data_for_create_out_picking_repair(self):
        vals = super()._catch_data_for_create_out_picking_repair()
        if self.crm_claim_id:
            vals["crm_claim_id"] = self.crm_claim_id.id
        return vals
