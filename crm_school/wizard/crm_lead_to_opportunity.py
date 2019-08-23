# Copyright 2019 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class CrmLead2OpportunityPartner(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'

    possible_partner_ids = fields.Many2many(
        comodel_name='res.partner', string='Possible Families', readonly=True)

    @api.model
    def default_get(self, fields):
        result = super(CrmLead2OpportunityPartner, self).default_get(fields)
        if self._context.get('active_id'):
            lead = self.env['crm.lead'].browse(self._context['active_id'])
            if not lead.future_student_ids:
                raise ValidationError(
                    _('There must be at least one future student.'))
            partners = self.env['res.partner']
            if lead.partner_id:  # a partner is set already
                partners |= lead.partner_id.id
            # search through the existing partners based on the lead's email
            if lead.email_from:
                partners |= partners.search(
                    [('email', '=', lead.email_from)])
            # search through the existing partners based on the lead's partner
            # or contact name
            if lead.partner_name:
                partners |= partners.search([
                    ('name', 'ilike', '%' + lead.partner_name + '%')])
            if lead.contact_name:
                contacts = partners.search([
                    ('name', 'ilike', '%' + lead.contact_name + '%')])
                partners |= contacts.mapped('commercial_partner_id')
            if lead.vat:
                contacts = partners.search([
                    ('vat', 'ilike', '%' + lead.vat + '%')])
                partners |= contacts.mapped('commercial_partner_id')
            result.update({
                'possible_partner_ids': [
                    (6, 0, partners.filtered(
                        lambda p: p.educational_category == 'family').ids)],
            })
        return result

    @api.multi
    def action_apply(self):
        lead_obj = self.env['crm.lead']
        if self.name != 'merge':
            for lead in lead_obj.browse(self._context.get('active_ids', [])):
                if not lead.future_student_ids:
                    raise ValidationError(
                        _('You must define a future student in the lead: {}.'
                          ).format(lead.name))
        return super(CrmLead2OpportunityPartner, self).action_apply()

    @api.onchange('team_id')
    def _onchange_team_id(self):
        if self.team_id and self.team_id.user_id:
            self.user_id = self.team_id.user_id
