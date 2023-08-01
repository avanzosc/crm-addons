# Copyright 2023 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    partner_shipping_id = fields.Many2one(
        string="Partner Shipping",
        comodel_name="res.partner")
    partner_invoice_id = fields.Many2one(
        string="Partner Invoice",
        comodel_name="res.partner")
    property_payment_term_id = fields.Many2one(
        string="Payment Term",
        comodel_name="account.payment.term",
        related="partner_id.property_payment_term_id",
        store=True)
    customer_payment_mode_id = fields.Many2one(
        string="Payment Mode",
        comodel_name="account.payment.mode",
        related="partner_id.customer_payment_mode_id",
        store=True)
    final_partner_id = fields.Many2one(
        string="Final User",
        comodel_name="res.partner")
    partner_company_id = fields.Many2one(
        string="Partner Company",
        comodel_name="res.partner",
        related="partner_id.parent_id",
        store=True)
    possible_partner_shipping_ids = fields.One2many(
        comodel_name="res.partner",
        compute="_compute_partner_shipping_ids")
    possible_partner_invoice_ids = fields.One2many(
        comodel_name="res.partner",
        compute="_compute_partner_invoice_ids")

    @api.depends("partner_id")
    def _compute_partner_shipping_ids(self):
        for line in self:
            possible_shippings = self.env['res.partner']
            if line.partner_id:
                possible_shippings += line.partner_company_id
                if line.partner_company_id.child_ids:
                    possible_shippings += (
                        line.partner_company_id.child_ids.filtered(
                            lambda c: c.type == 'delivery'))
                if line.partner_company_id.parent_id:
                    possible_shippings += line.partner_company_id.parent_id
                    if line.partner_company_id.parent_id.child_ids:
                        possible_shippings += line.partner_company_id.parent_id.child_ids.filtered(lambda c: c.type == 'delivery')
            line.possible_partner_shipping_ids = [(6, 0, possible_shippings.ids)]

    @api.depends("partner_id")
    def _compute_partner_invoice_ids(self):
        for line in self:
            possible_invoice = self.env['res.partner']
            if line.partner_id:
                possible_invoice += line.partner_company_id
                if line.partner_company_id.child_ids:
                    possible_invoice += (
                        line.partner_company_id.child_ids.filtered(
                            lambda c: c.type == 'invoice'))
                if line.partner_company_id.parent_id:
                    possible_invoice += line.partner_company_id.parent_id
                    if line.partner_company_id.parent_id.child_ids:
                        possible_invoice += line.partner_company_id.parent_id.child_ids.filtered(lambda c: c.type == 'invoice')
            line.possible_partner_invoice_ids = [(6, 0, possible_invoice.ids)]

