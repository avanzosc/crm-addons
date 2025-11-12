# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import tagged

from .common import CrmClaimCommon


@tagged("post_install", "-at_install")
class TestCrmClaimClose(CrmClaimCommon):
    def test_crm_claim_close(self):
        new_claim = self.claim_model.create(
            {
                "name": "Test Claim",
                "stage_id": self.close_stage.id,
            }
        )
        self.assertTrue(new_claim.stage_id.closed)
        self.assertTrue(new_claim.date_closed)
        new_claim.write(
            {
                "stage_id": self.open_stage.id,
            }
        )
        self.assertFalse(new_claim.stage_id.closed)
        self.assertFalse(new_claim.date_closed)
        new_claim.write(
            {
                "stage_id": self.close_stage.id,
            }
        )
        self.assertTrue(new_claim.stage_id.closed)
        self.assertTrue(new_claim.date_closed)
