# Copyright 2019 Alfredo de la fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    @api.depends('birthdate_date')
    def _compute_year_birth(self):
        for res in self.filtered(lambda c: c.birthdate_date):
            res.year_birth = fields.Date.from_string(res.birthdate_date).year

    year_birth = fields.Integer(
        string='Year of birth', compute='_compute_year_birth', store=True)
