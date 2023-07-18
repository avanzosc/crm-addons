# Copyright 2023 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    final_partner_id = fields.Many2one(
        string="Final User",
        comodel_name="res.partner")

    @api.onchange('opportunity_id')
    def onchange_opportunity_id(self):
        if self.opportunity_id:
            self.write({
                "partner_invoice_id": (
                    self.opportunity_id.partner_invoice_id.id),
                "partner_shipping_id": (
                    self.opportunity_id.partner_shipping_id.id),
                "payment_term_id": (
                    self.opportunity_id.property_payment_term_id.id),
                "payment_mode_id": (
                    self.opportunity_id.customer_payment_mode_id.id),
                "final_partner_id": self.opportunity_id.final_partner_id.id})
