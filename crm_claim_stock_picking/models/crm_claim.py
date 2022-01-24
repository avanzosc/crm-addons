# Copyright 2021 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, _, api


class CrmClaim(models.Model):
    _inherit = 'crm.claim'

    def _compute_picking_count(self):
        for claim in self:
            claim.picking_count = len(claim.picking_ids)

    def _compute_picking_ids(self):
        for claim in self:
            cond = ['|', ('id', '=', claim.picking_id.id), (
                'claim_id', '=', claim.id)]
            pickings = self.env['stock.picking'].search(cond)
            claim.picking_ids = [(6, 0, pickings.ids)]

    picking_ids = fields.Many2many(
        string='Transfers', comodel_name='stock.picking',
        compute='_compute_picking_ids')
    picking_count = fields.Integer(
        '# Transfers', compute='_compute_picking_count')
    picking_id = fields.Many2one(
        string='Transfer', comodel_name='stock.picking')
    second_model_ref_id = fields.Reference(
        selection="_selection_model", string="Second Model Reference"
    )

    @api.model
    def _selection_model(self):
        result = super(CrmClaim, self)._selection_model()
        result.append(('stock.move', _('Stock Move')))
        return result

    def action_view_picking(self):
        context = self.env.context.copy()
        context.update({'default_claim_id': self.id})
        if self.partner_id:
            context.update({'default_partner_id': self.partner_id.id})
        return {
            'name': _("Transfers"),
            'view_mode': 'tree,form',
            'res_model': 'stock.picking',
            'domain': [('id', 'in', self.picking_ids.ids)],
            'type': 'ir.actions.act_window',
            'context': context
        }

    @api.onchange('model_ref_id')
    def onchange_model_ref_id(self):
        if self.model_ref_id:
            self.name = u'{} {}'.format(
                self.name, self.model_ref_id.name)
