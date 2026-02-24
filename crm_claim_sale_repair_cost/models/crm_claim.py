# Copyright 2025 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    sale_repair_id = fields.Many2one(
        string="Sale Repair",
        comodel_name="sale.order",
        copy=False,
        store=True,
        compute="_compute_sale_repair_id",
    )
    sale_repair_cost = fields.Float(
        string="Sale Repair Total Cost",
        digits="Product Price",
        copy=False,
        store=True,
        related="sale_repair_id.sale_order_cost",
    )
    sale_repair_qty_ordered = fields.Float(
        string="Sale Repair Qty Ordered",
        digits="Product Unit of Measure",
        copy=False,
        store=True,
        related="sale_repair_id.qty_ordered",
    )

    sale_repair_qty_delivered = fields.Float(
        string="Sale Repair Qty Delivered",        
        digits="Product Unit of Measure",
        copy=False,
        store=True,
        related="sale_repair_id.qty_delivered",
    )

    @api.depends("model_ref_id", "ref2", "ref3")
    def _compute_sale_repair_id(self):
        for claim in self:
            sale_repair_id = self.env["sale.order"]
            if claim.model_ref_id:
                sale_repair_id = claim._search_sale_order_repair_cost(
                    claim.model_ref_id
                )
            if not sale_repair_id and claim.ref2:
                sale_repair_id = claim._search_sale_order_repair_cost(claim.ref2)
            if not sale_repair_id and claim.ref3:
                sale_repair_id = claim._search_sale_order_repair_cost(claim.ref3)
            claim.sale_repair_id = sale_repair_id

    def _search_sale_order_repair_cost(self, modelref):
        if str(modelref._name) == "sale.order" and modelref.is_repair:
            return modelref.id
        return self.env["sale.order"]
