# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    def _get_values_to_create_repair_order(self):
        vals = super(CrmLead, self)._get_values_to_create_repair_order()
        if self.partner_shipping_id:
            vals["address_id"] = self.partner_shipping_id.id
        return vals
