# Copyright 2015 Pedro M. Baeza (http://www.serviciosbaeza.com)
# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# Copyright 2026 Eñaut Alberdi - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    @api.depends("model_ref_id")
    def _compute_ref_model_name(self):
        model_obj = self.env["ir.model"]
        for claim in self:
            ref_model_name = False
            if claim.model_ref_id:
                cond = [("model", "=", str(claim.model_ref_id._name))]
                model = model_obj.search(cond, limit=1)
                ref_model_name = model.display_name
            claim.ref_model_name = ref_model_name

    @api.depends("model_ref_id")
    def _compute_ref_name(self):
        for claim in self:
            ref_name = False
            if claim.model_ref_id:
                ref_name = claim.model_ref_id.display_name
            claim.ref_name = ref_name

    ref_model_name = fields.Char(
        string="Ref. Model", compute="_compute_ref_model_name", store=True, copy=False
    )
    ref_name = fields.Char(
        string="Ref. Name", compute="_compute_ref_name", store=True, copy=False
    )
