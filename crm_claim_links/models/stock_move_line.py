from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    claim_id = fields.Many2one(
        string="Claim", comodel_name="crm.claim",
        related="picking_id.claim_id", store=True, copy=False
    )
