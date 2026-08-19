# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import tagged

from .common import CrmClaimNonConformityCommon


@tagged("post_install", "-at_install")
class TestCrmClaimTypeNonConformity(CrmClaimNonConformityCommon):
    def test_claim_type_non_conformity_field(self):
        self.assertTrue(self.non_conformity_type.non_conformity)
        self.assertFalse(self.normal_type.non_conformity)

    def test_claim_type_write_non_conformity(self):
        self.normal_type.write({"non_conformity": True})
        self.assertTrue(self.normal_type.non_conformity)
        self.non_conformity_type.write({"non_conformity": False})
        self.assertFalse(self.non_conformity_type.non_conformity)


@tagged("post_install", "-at_install")
class TestCrmClaimNonConformity(CrmClaimNonConformityCommon):
    def test_claim_fields_exist(self):
        claim = self.claim_model.create(
            {
                "name": "Test Claim Fields",
                "stage_id": self.open_stage.id,
            }
        )
        self.assertTrue(hasattr(claim, "non_conformity"))
        self.assertTrue(hasattr(claim, "cost"))
        self.assertTrue(hasattr(claim, "lot_id"))
        self.assertTrue(hasattr(claim, "contact_id"))
        self.assertTrue(hasattr(claim, "immediate_action"))

    def test_claim_non_conformity_default_false(self):
        claim = self.claim_model.create(
            {
                "name": "Test Default Non Conformity",
                "stage_id": self.open_stage.id,
            }
        )
        self.assertFalse(claim.non_conformity)

    def test_claim_non_conformity_default_from_context(self):
        claim = self.claim_model.with_context(non_conformity=True).create(
            {
                "name": "Test Context Non Conformity",
                "stage_id": self.open_stage.id,
            }
        )
        self.assertTrue(claim.non_conformity)

    def test_claim_non_conformity_default_false_from_context(self):
        claim = self.claim_model.with_context(non_conformity=False).create(
            {
                "name": "Test Context False",
                "stage_id": self.open_stage.id,
            }
        )
        self.assertFalse(claim.non_conformity)

    def test_claim_default_claim_type_with_non_conformity_context(self):
        claim = self.claim_model.with_context(non_conformity=True).create(
            {
                "name": "Test Default Claim Type NC",
                "stage_id": self.open_stage.id,
            }
        )
        self.assertEqual(claim.claim_type, self.non_conformity_type)

    def test_claim_default_claim_type_without_non_conformity_context(self):
        claim = self.claim_model.create(
            {
                "name": "Test Default Claim Type Normal",
                "stage_id": self.open_stage.id,
            }
        )
        self.assertFalse(claim.claim_type)

    def test_claim_cost_field(self):
        claim = self.claim_model.create(
            {
                "name": "Test Cost Field",
                "stage_id": self.open_stage.id,
                "cost": 150.75,
            }
        )
        self.assertAlmostEqual(claim.cost, 150.75, places=2)

    def test_claim_cost_default_zero(self):
        claim = self.claim_model.create(
            {
                "name": "Test Cost Default",
                "stage_id": self.open_stage.id,
            }
        )
        self.assertEqual(claim.cost, 0.0)

    def test_claim_contact_id_field(self):
        claim = self.claim_model.create(
            {
                "name": "Test Contact Field",
                "stage_id": self.open_stage.id,
                "contact_id": self.partner.id,
            }
        )
        self.assertEqual(claim.contact_id, self.partner)

    def test_claim_immediate_action_field(self):
        claim = self.claim_model.create(
            {
                "name": "Test Immediate Action",
                "stage_id": self.open_stage.id,
                "immediate_action": "Replace defective part immediately",
            }
        )
        self.assertEqual(claim.immediate_action, "Replace defective part immediately")

    def test_claim_lot_id_field(self):
        claim = self.claim_model.create(
            {
                "name": "Test Lot Field",
                "stage_id": self.open_stage.id,
            }
        )
        self.assertFalse(claim.lot_id)

    def test_onchange_non_conformity_true(self):
        claim = self.claim_model.new({"non_conformity": True})
        result = claim.onchange_non_conformity()
        self.assertIn("domain", result)
        self.assertEqual(
            result["domain"]["claim_type"],
            [("non_conformity", "=", True)],
        )

    def test_onchange_non_conformity_false(self):
        claim = self.claim_model.new({"non_conformity": False})
        result = claim.onchange_non_conformity()
        self.assertIn("domain", result)
        self.assertEqual(
            result["domain"]["claim_type"],
            [("non_conformity", "=", False)],
        )

    def test_claim_write_non_conformity_and_cost(self):
        claim = self.claim_model.create(
            {
                "name": "Test Write Fields",
                "stage_id": self.open_stage.id,
            }
        )
        claim.write(
            {
                "non_conformity": True,
                "cost": 250.0,
                "immediate_action": "Immediate corrective action",
                "contact_id": self.partner.id,
            }
        )
        self.assertTrue(claim.non_conformity)
        self.assertEqual(claim.cost, 250.0)
        self.assertEqual(claim.immediate_action, "Immediate corrective action")
        self.assertEqual(claim.contact_id, self.partner)

    def test_claim_claim_type_change(self):
        claim = self.claim_model.create(
            {
                "name": "Test Claim Type Change",
                "stage_id": self.open_stage.id,
                "claim_type": self.normal_type.id,
            }
        )
        self.assertEqual(claim.claim_type, self.normal_type)
        self.assertFalse(claim.claim_type.non_conformity)
        claim.write({"claim_type": self.non_conformity_type.id})
        self.assertEqual(claim.claim_type, self.non_conformity_type)
        self.assertTrue(claim.claim_type.non_conformity)

    def test_claim_cost_copy_false(self):
        claim = self.claim_model.create(
            {
                "name": "Test Cost Copy",
                "stage_id": self.open_stage.id,
                "cost": 500.0,
            }
        )
        claim_copy = claim.copy()
        self.assertEqual(claim_copy.cost, 0.0)


@tagged("post_install", "-at_install")
class TestResUsersSign(CrmClaimNonConformityCommon):
    def test_res_users_has_sign_field(self):
        user = self.env.user
        self.assertTrue(hasattr(user, "sign"))

    def test_res_users_sign_field_empty_by_default(self):
        user = self.env.user
        self.assertFalse(user.sign)


@tagged("post_install", "-at_install")
class TestCrmClaimNonConformityReport(CrmClaimNonConformityCommon):
    def test_report_model_exists(self):
        self.assertTrue(self.env["crm.claim.non.conformity.report"]._auto is False)

    def test_report_with_non_conformity_claim(self):
        self.claim_model.with_context(non_conformity=True).create(
            {
                "name": "Test NC for Report",
                "stage_id": self.open_stage.id,
                "cost": 100.0,
            }
        )
        self.env.cr.execute("SELECT count(*) FROM crm_claim_non_conformity_report")
        result = self.env.cr.fetchone()
        self.assertIsNotNone(result)
