# Copyright 2020 Adrian Revilla - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class CRMlead(models.Model):
    _inherit = 'crm.lead'

    shipping_comercial_name = fields.Char(string='Comercial name')
    shipping_billing_phone = fields.Char(string='Billing phone')
    shipping_billing_email = fields.Char(string='Billing email')

    shipping_sending_street = fields.Char(
        string='Sending street', readonly=False)
    shipping_sending_street2 = fields.Char(string='Sending street2')
    shipping_sending_zip = fields.Char(
        string='Sending zip', change_default=True)
    shipping_sending_city = fields.Char(string='Sending city')
    shipping_sending_state_id = fields.Many2one(
        comodel_name="res.country.state", string='Sending state')
    shipping_sending_country_id = fields.Many2one(
        comodel_name='res.country', string='Sending country')
    shipping_sending_phone = fields.Char(string='Sending phone')
    shipping_sending_email = fields.Char(string='Sending email')
