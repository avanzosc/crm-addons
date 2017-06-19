# -*- coding: utf-8 -*-
# Copyright © 2017 Oihane Crucelaegui - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp.addons.crm_lead_vat.tests.test_lead import LeadCase


class TestCrmLeadPayment(LeadCase):
    def setUp(self):
        super(TestCrmLeadPayment, self).setUp()
        self.test_payment_term = self.env['account.payment.term'].create({
            'name': __file__,
        })
        journal = self.env['account.journal'].search([
            ('type', 'in', ('bank', 'cash'))])
        bank = self.env['res.partner.bank'].search([])
        self.test_payment_mode = self.env['payment.mode'].create({
            'name': __file__,
            'type': self.ref(
                'account_banking_payment_export.manual_bank_tranfer'),
            'sale_ok': True,
            'journal': journal[:1].id,
            'bank_id': bank[:1].id,

        })

    def test_transfered_values(self):
        """Field gets transfered when creating partner."""
        super(TestCrmLeadPayment, self).test_transfered_values()
        self.lead.partner_id = False
        self.lead.write({
            'partner_id': False,
            'property_payment_term': self.test_payment_term.id,
            'customer_payment_mode': self.test_payment_mode.id,
        })
        self.lead.handle_partner_assignation()
        self.assertEqual(
            self.lead.partner_id.property_payment_term, self.test_payment_term)
        self.assertEqual(
            self.lead.partner_id.customer_payment_mode, self.test_payment_mode)

    def test_onchange_partner_id(self):
        """Lead gets payment data from partner when linked to it."""
        super(TestCrmLeadPayment, self).test_onchange_partner_id()
        self.partner.write({
            'property_payment_term': self.test_payment_term.id,
            'customer_payment_mode': self.test_payment_mode.id,
        })
        result = self.lead.on_change_partner_id(self.partner.id)
        self.assertEqual(
            result["value"]["property_payment_term"],
            self.test_payment_term.id)
        self.assertEqual(
            result["value"]["customer_payment_mode"],
            self.test_payment_mode.id)
