# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import common


class CrmClaimNonConformityCommon(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.claim_type_model = cls.env["crm.claim.type"]
        cls.claim_model = cls.env["crm.claim"].with_context(
            mail_create_nosubscribe=True
        )
        cls.claim_stage_model = cls.env["crm.claim.stage"]

        cls.open_stage = cls.claim_stage_model.search([], limit=1, order="sequence asc")

        cls.non_conformity_type = cls.claim_type_model.create(
            {
                "name": "Test Non Conformity Type",
                "non_conformity": True,
            }
        )
        cls.normal_type = cls.claim_type_model.create(
            {
                "name": "Test Normal Claim Type",
                "non_conformity": False,
            }
        )
        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Test Partner NC",
            }
        )
