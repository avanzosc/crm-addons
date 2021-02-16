# Copyright 2020 Adrian Revilla - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError, MissingError


class WebsiteContact(http.Controller):

    @http.route('/contactus', type='http', auth="public", website=True)
    def websiteContactUs(self):
        state_ids = request.env['res.country.state'].search([])
        country_ids = request.env['res.country'].search([])
        values = {'state_ids': state_ids,
                  'country_ids': country_ids}
        return http.request.render('website.contactus', values)

    @http.route('/contactus_getdata', type='http', auth="public", website=True)
    def websiteContactData(self):
        state_ids = request.env['res.country.state'].search([])
        country_ids = request.env['res.country'].search([])
        values = {'state_ids': state_ids,
                  'country_ids': country_ids}
        return http.request.render('website.contactus', values)

    @http.route('/contactus_send',
                type='http', auth="public", website=True)
    def websiteContact(self, **kwargs):
        crm_lead_values = {
            'contact_name': kwargs['contact_name'],
            'phone': kwargs['phone'],
            'email_from': kwargs['email_from'],
            'partner_name': kwargs['partner_name'],
            'sending_street': kwargs['shipping_sending_street'],
            'sending_city': kwargs['shipping_sending_city'],
            'sending_state_id': kwargs['shipping_sending_state_id'],
            'sending_zip': kwargs['shipping_sending_zip'],
            'sending_country_id': kwargs['shipping_sending_country_id'],
            'comercial_name': kwargs['shipping_comercial_name'],
            'billing_phone': kwargs['shipping_billing_phone'],
            'billing_email': kwargs['shipping_billing_email'],
            'name': kwargs['name'],
            'description': kwargs['description'],
            'mobile': kwargs['mobile'],
            'vat': kwargs['vat'],
            'street': kwargs['street'],
            'city': kwargs['city'],
            'state_id': kwargs['state_id'],
            'zip': kwargs['zip'],
            'country_id': kwargs['country_id'],
            'website': kwargs['website'],
            'sending_phone': kwargs['shipping_sending_phone'],
            'sending_email': kwargs['shipping_sending_email'],
            }
        try:
            crm_lead = request.env['crm.lead'].sudo().create(crm_lead_values)
            if crm_lead:
                msg_text = 'OK. CRM Lead Created!'
            else:
                msg_text = 'ERROR. CRM Lead Not Created!'
            values = {
                'msg_text': msg_text,
                'crm_lead': crm_lead}
            return http.request.render(
                'website_crm_extended_address.extended_send_contactus_form',
                values)
        except (AccessError, MissingError):
            values = {
                'msg_text': 'ERROR. Something Wrong Occurred!',
                'mail_text': 'ERROR. Something Wrong Occurred!'}
            return http.request.render(
                'website_crm_extended_address.extended_send_contactus_form',
                values)
