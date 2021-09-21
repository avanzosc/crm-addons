# Copyright 2021 Berezi - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models


class CrmPhonecall(models.Model):
    _inherit = 'crm.phonecall'

    def create_lead_opportunity(self):
        vals = {'name': self.name,
                'description': self.description,
                'team_id': self.team_id,
                'priority': self.priority}
        if self.partner_id:
            vals.update({'partner_id': self.partner_id.id,
                         'phone': self.partner_phone,
                         'mobile': self.partner_mobile,
                         'email_from': self.partner_id.email,
                         'type': 'opportunity'})
        if not self.partner_id:
            vals['type'] = 'lead'
        lead_oppor = self.env['crm.lead'].create(vals)
        self.opportunity_id = lead_oppor.id
