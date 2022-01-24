# Copyright 2021 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _compute_count_claim(self):
        for picking in self:
            picking.count_claim = len(picking.claim_ids)

    def _compute_claim_ids(self):
        for picking in self:
            cond = ['|', ('id', '=', picking.claim_id.id), (
                'picking_id', '=', picking.id)]
            claims = self.env['crm.claim'].search(cond)
            picking.claim_ids = [(6, 0, claims.ids)]

    claim_ids = fields.Many2many(
        string="Claims",
        comodel_name="crm.claim",
        compute='_compute_claim_ids')
    count_claim = fields.Integer('# Claims', compute='_compute_count_claim')
    claim_id = fields.Many2one(
        string='Claim', comodel_name='crm.claim')

    def action_view_claim(self):
        context = self.env.context.copy()
        today = fields.Date.today()
        context.update({'default_picking_id': self.id,
                        'default_name': u'{} {}'.format(today,
                                                        self.partner_id.name)})
        if self.partner_id:
            context.update({'default_partner_id': self.partner_id.id})
        return {
            'name': _("Claims"),
            'view_mode': 'tree,form',
            'res_model': 'crm.claim',
            'domain': [('id', 'in', self.claim_ids.ids)],
            'type': 'ir.actions.act_window',
            'context': context,
        }
