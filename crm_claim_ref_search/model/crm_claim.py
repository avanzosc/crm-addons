# Copyright 2015 Pedro M. Baeza (http://www.serviciosbaeza.com)
# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# Copyright 2026 Eñaut Alberdi - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    def _get_model_ref(self):
        self.ensure_one()
        try:
            return self.model_ref_id
        except KeyError:
            return False

    @api.depends("model_ref_id")
    def _compute_ref_model_name(self):
        model_obj = self.env["ir.model"]
        for claim in self:
            ref_model_name = False
            model_ref = claim._get_model_ref()
            if model_ref:
                cond = [("model", "=", str(model_ref._name))]
                model = model_obj.search(cond, limit=1)
                ref_model_name = model.display_name
            claim.ref_model_name = ref_model_name

    @api.depends("model_ref_id")
    def _compute_ref_name(self):
        for claim in self:
            ref_name = False
            model_ref = claim._get_model_ref()
            if model_ref and model_ref.exists():
                ref_name = model_ref.display_name
            claim.ref_name = ref_name

    ref_model_name = fields.Char(
        string="Ref. Model", compute="_compute_ref_model_name", store=True, copy=False
    )
    ref_name = fields.Char(
        string="Ref. Name", compute="_compute_ref_name", store=True, copy=False
    )
