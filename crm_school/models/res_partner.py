# Copyright 2019 Alfredo de la fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, fields, models

str2date = fields.Date.from_string


class ResPartner(models.Model):
    _inherit = 'res.partner'

    year_birth = fields.Integer(
        string='Year of birth', compute='_compute_year_birth', store=True)

    @api.multi
    @api.depends('birthdate_date')
    def _compute_year_birth(self):
        for res in self.filtered(lambda c: c.birthdate_date):
            res.year_birth = str2date(res.birthdate_date).year


class ResPartnerFamily(models.Model):
    _inherit = 'res.partner.family'

    crm_lead_id = fields.Many2one(
        string='Lead', comodel_name='crm.lead')
