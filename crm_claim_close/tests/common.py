# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import common


class CrmClaimCommon(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.claim_model = cls.env["crm.claim"].with_context(
            mail_create_nosubscribe=True
        )
        claim_stage_model = cls.env["crm.claim.stage"]

        cls.open_stage = claim_stage_model.search([("closed", "=", False)], limit=1)
        cls.close_stage = claim_stage_model.search([("closed", "=", True)], limit=1)
