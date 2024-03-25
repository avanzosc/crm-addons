# Copyright 2021 Daniel Campos - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import tagged

from .common import CrmClaimCorrectiveCommon


@tagged("post_install", "-at_install")
class TestACrmClaimCorrective(CrmClaimCorrectiveCommon):
    def test_crm_claim_corrective_name(self):
        new_name = self._get_next_name()
        corrective = self.corrective_model.create({"name": "/"})
        self.assertEqual(corrective.name, new_name)

    def test_crm_claim_onchange(self):
        self.claim.claim_description_id = self.claim_descrp.id
        self.claim.onchange_claim_description()
        self.assertEqual(self.claim.description, self.claim_descrp.description)
        self.claim.cause_description_id = self.cause_descrp.id
        self.claim.onchange_cause_description()
        self.assertEqual(self.claim.cause, self.cause_descrp.description)
        self.claim.resolution_description_id = self.resolution_descrp.id
        self.claim.onchange_resolution_description()
        self.assertEqual(self.claim.resolution, self.resolution_descrp.description)

    def test_crm_claim_create_corrective(self):
        self.assertFalse(self.claim.corrective_id)
        self.claim.button_create_corrective()
        self.assertTrue(self.claim.corrective_id)
        self.assertEqual(self.claim, self.claim.corrective_id.claim_id)

    def _get_next_name(self):
        return self.corrective_sequence.get_next_char(
            self.corrective_sequence.number_next_actual
        )
