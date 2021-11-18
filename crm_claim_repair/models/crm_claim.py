# Copyright 2021 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, _


class CrmClaim(models.Model):
    _inherit = 'crm.claim'

    def _compute_repair_count(self):
        for claim in self:
            claim.repair_count = len(claim.repair_ids)

    repair_ids = fields.One2many(
        string='Repair Orders', comodel_name='repair.order',
        inverse_name='claim_id')
    repair_count = fields.Integer(
        '# Repair Orders', compute='_compute_repair_count')

    def action_view_repair(self):
        context = self.env.context.copy()
        context.update({'default_claim_id': self.id})
        return {
            'name': _("Repair Orders"),
            'view_mode': 'tree,form',
            'res_model': 'repair.order',
            'domain': [('id', 'in', self.repair_ids.ids)],
            'type': 'ir.actions.act_window',
            'context': context
        }
