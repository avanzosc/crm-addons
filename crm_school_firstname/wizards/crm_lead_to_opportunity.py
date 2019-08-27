# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class CrmLead2OpportunityPartner(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'

    @api.model
    def default_get(self, fields):
        result = super(CrmLead2OpportunityPartner, self).default_get(fields)
        if self._context.get('active_id'):
            lead = self.env['crm.lead'].browse(self._context['active_id'])
            partner_ids = (
                result.get('possible_partner_ids')[0][2] if (
                    'possible_partner_ids' in result) else [])
            partners = self.env['res.partner'].browse(partner_ids)
            # search through the existing partners based on the lead's contact
            # firstname and lastname
            if lead.contact_name and lead.contact_lastname:
                contacts = partners.search([
                    ('firstname', 'ilike', '%' + lead.contact_name + '%'),
                    ('lastname', 'ilike', '%' + lead.contact_lastname + '%')])
                partners |= contacts.mapped('commercial_partner_id')
            if lead.contact_lastname:
                contacts = partners.search([
                    ('lastname', 'ilike', '%' + lead.contact_lastname + '%')])
                partners |= contacts.mapped('commercial_partner_id')
            result.update({
                'possible_partner_ids': [
                    (6, 0, partners.filtered(
                        lambda p: p.educational_category == 'family').ids)],
            })
        return result
