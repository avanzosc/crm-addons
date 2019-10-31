# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo.tests import common
from odoo.modules.module import get_module_resource


@common.at_install(False)
@common.post_install(True)
class TestCrmClaimSchool(common.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super(TestCrmClaimSchool, cls).setUpClass()
        cls.claim_model = cls.env['crm.claim']
        cls.category_model = cls.env['crm.claim.category']
        cls.user = cls.env['res.users'].create({
            'company_id': cls.env.ref("base.main_company").id,
            'name': "Crm Salesman",
            'login': "csu",
            'email': "crmuser@yourcompany.com",
            'groups_id': [
                (4, cls.env.ref('sales_team.group_sale_salesman').id)],
        })
        cls.team = cls.env['crm.team'].create({
            'name': 'Test Team',
            'user_id': cls.user.id,
            'member_ids': [(6, 0, cls.user.ids)],
        })
        cls.category = cls.category_model.create({
            'name': 'Test Category',
            'team_id': cls.team.id,
        })
        cls.category2 = cls.category.create({
            'name': 'Test Category 2',
        })
        cls.fetchmail_server = cls.env['fetchmail.server'].create({
            'name': 'Test Mail Server',
            'type': 'imap',
            'claim_category_ids': [(6, 0, cls.category.ids)],
        })

    def test_crm_claim_message(self):
        with open(get_module_resource(
            'crm_claim_school', 'tests', 'customer_request.eml'), 'rb') as \
                request_file:
            request_message = request_file.read()
        self.env['mail.thread'].with_context(
            fetchmail_server_id=self.fetchmail_server.id).message_process(
                'crm.claim', request_message)
        claim = self.env['crm.claim'].search(
            [('email_from', '=', 'Mr. John Right <info@customer.com>')],
            limit=1)
        self.assertTrue(claim, 'Failed to create claim')
        self.assertEquals(claim.categ_id, self.category)
        self.assertEquals(claim.team_id, self.team)
        self.assertEquals(claim.user_id, self.user)

    def test_crm_claim_message_2categories(self):
        self.fetchmail_server.claim_category_ids = [(4, self.category2.id)]
        self.assertEquals(len(self.fetchmail_server.claim_category_ids), 2)
        with open(get_module_resource(
            'crm_claim_school', 'tests', 'customer_request.eml'), 'rb') as \
                request_file:
            request_message = request_file.read()
        self.env['mail.thread'].with_context(
            fetchmail_server_id=self.fetchmail_server.id).message_process(
                'crm.claim', request_message)
        claim = self.env['crm.claim'].search(
            [('email_from', '=', 'Mr. John Right <info@customer.com>')],
            limit=1)
        self.assertTrue(claim, 'Failed to create claim')
        self.assertFalse(claim.categ_id)

    def test_crm_claim(self):
        claim = self.claim_model.create({
            'name': 'New Claim',
            'categ_id': self.category.id,
        })
        self.assertNotEquals(claim.team_id, claim.categ_id.team_id)
        self.assertNotIn(self.user, claim.team_users_ids)
        claim.onchange_categ_id()
        self.assertEquals(claim.team_id, claim.categ_id.team_id)
        self.assertEquals(claim.user_id, claim.categ_id.team_id.user_id)
        self.assertIn(self.user, claim.team_users_ids)
