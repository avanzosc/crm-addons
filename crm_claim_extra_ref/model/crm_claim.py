from odoo import _, api, models, fields
APPLICABLE_MODELS = [
    "account.invoice",
    "event.registration",
    "hr.applicant",
    "res.partner",
    "product.product",
    "purchase.order",
    "purchase.order.line",
    "sale.order",
    "sale.order.line",
]


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    def _links_get(self):
        return [
            (x, _(self.env[x]._description)) for x in
            APPLICABLE_MODELS if x in self.env
        ]

    @api.depends("ref2")
    def _compute_ref_model_name2(self):
        model_obj = self.env["ir.model"]
        for claim in self:
            ref_model_name2 = False
            if claim.ref2:
                cond = [("model", "=", str(claim.ref2._name))]
                model = model_obj.search(cond)
                ref_model_name2 = model.name
            claim.ref_model_name2 = ref_model_name2

    @api.depends("ref2")
    def _compute_ref_name2(self):
        for claim in self:
            ref_name2 = False
            if claim.ref2:
                ref_name2 = claim.ref2.name_get()[0][1]
            claim.ref_name2 = ref_name2

    @api.depends("ref3")
    def _compute_ref_model_name3(self):
        model_obj = self.env["ir.model"]
        for claim in self:
            ref_model_name3 = False
            if claim.ref3:
                cond = [("model", "=", str(claim.ref3._name))]
                model = model_obj.search(cond)
                ref_model_name3 = model.name
            claim.ref_model_name3 = ref_model_name3

    @api.depends("ref3")
    def _compute_ref_name3(self):
        for claim in self:
            ref_name3 = False
            if claim.ref3:
                ref_name3 = claim.ref3.name_get()[0][1]
            claim.ref_name3 = ref_name3

    ref2 = fields.Reference(
        string="Reference 2", selection="_links_get"
    )
    ref_model_name2 = fields.Char(
        string="Ref. Model 2", compute="_compute_ref_model_name2", store=True
    )
    ref_name2 = fields.Char(
        string="Ref. Name 2", compute="_compute_ref_name2", store=True
    )
    ref3 = fields.Reference(
        string="Reference 3", selection="_links_get"
    )
    ref_model_name3 = fields.Char(
        string="Ref. Model 3", compute="_compute_ref_model_name3", store=True
    )
    ref_name3 = fields.Char(
        string="Ref. Name 3", compute="_compute_ref_name3", store=True
    )
