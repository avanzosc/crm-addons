# Copyright 2021 Daniel Campos - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    photo1 = fields.Binary(string="Photo1", attachment=True)
    photo2 = fields.Binary(string="Photo2", attachment=True)
    photo3 = fields.Binary(string="Photo3", attachment=True)
    photo4 = fields.Binary(string="Photo4", attachment=True)
    claim_description_id = fields.Many2one(
        comodel_name="crm.claim.description",
        string="Claim Description",
        domain="[('type_description', '=', 'claim')]",
    )
    cause_description_id = fields.Many2one(
        comodel_name="crm.claim.description",
        string="Cause Description",
        domain="[('type_description', '=', 'cause')]",
    )
    resolution_description_id = fields.Many2one(
        comodel_name="crm.claim.description",
        string="Resolution Description",
        domain="[('type_description','=', 'resolution')]",
    )
    corrective_id = fields.Many2one(
        comodel_name="crm.claim.corrective", string="Claim Corrective"
    )

    @api.onchange("claim_description_id")
    def onchange_claim_description(self):
        if self.claim_description_id:
            self.description = self.claim_description_id.description

    @api.onchange("cause_description_id")
    def onchange_cause_description(self):
        if self.cause_description_id:
            self.cause = self.cause_description_id.description

    @api.onchange("resolution_description_id")
    def onchange_resolution_description(self):
        if self.resolution_description_id:
            self.resolution = self.resolution_description_id.description

    @api.onchange("corrective_id")
    def onchange_claim_corrective(self):
        if self.corrective_id:
            self.corrective_id.claim_id = self._origin.id

    def button_create_corrective(self):
        corrective_obj = self.env["crm.claim.corrective"]
        for claim in self.filtered(lambda r: not r.corrective_id):
            corrective = corrective_obj.create(
                {
                    "claim_id": claim.id,
                }
            )
            claim.corrective_id = corrective


class CrmClaimDescription(models.Model):
    _name = "crm.claim.description"
    _description = "Claim Description"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    type_description = fields.Selection(
        selection=[
            ("claim", "Claim Description"),
            ("cause", "Cause Description"),
            ("resolution", "Resolution Description"),
        ],
        string="Description Type",
    )
