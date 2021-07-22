# Copyright 2021 Daniel Campos - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import common


class CrmClaimCorrectiveCommon(common.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super(CrmClaimCorrectiveCommon, cls).setUpClass()
        cls.corrective_model = cls.env["crm.claim.corrective"]
        cls.claim_descrp_model = cls.env["crm.claim.description"]
        cls.corrective_sequence = cls.env.ref(
            "crm_claim_corrective.seq_corrective_action")
        cls.claim_model = cls.env["crm.claim"].with_context(
            mail_create_nosubscribe=True)
        cls.claim = cls.claim_model.create({
            "name": "Test Claim",
            "team_id": cls.env.ref("sales_team.salesteam_website_sales").id,
            }
        )
        cls.claim_descrp = cls.claim_descrp_model.create({
            "name": "Claim description",
            "description": "This is a claim description",
            "type_description": "claim",
        })
        cls.cause_descrp = cls.claim_descrp_model.create({
            "name": "Cause description",
            "description": "This is a cause description",
            "type_description": "cause",
        })
        cls.resolution_descrp = cls.claim_descrp_model.create({
            "name": "Resolution description",
            "description": "This is a resolution description",
            "type_description": "resolution",
        })
