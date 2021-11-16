# Copyright 2021 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, _


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def _compute_claim_count(self):
        for production in self:
            production.claim_count = len(production.claim_ids)

    claim_ids = fields.One2many(
        string='Claims', comodel_name='crm.claim',
        inverse_name='production_id')
    claim_count = fields.Integer(
        '# Claims', compute='_compute_claim_count')

    def action_view_claim(self):
        context = self.env.context.copy()
        context.update({'default_production_id': self.id})
        print(context)
        return {
            'name': _("Claims"),
            'view_mode': 'tree,form',
            'res_model': 'crm.claim',
            'domain': [('id', 'in', self.claim_ids.ids)],
            'type': 'ir.actions.act_window',
            'context': context
        }
