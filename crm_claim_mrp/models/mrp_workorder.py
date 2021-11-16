# Copyright 2021 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, _


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    def _compute_claim_count(self):
        for workorder in self:
            workorder.claim_count = len(workorder.claim_ids)

    claim_ids = fields.One2many(
        string='Claims', comodel_name='crm.claim',
        inverse_name='workorder_id')
    claim_count = fields.Integer(
        '# Claims', compute='_compute_claim_count')

    def action_view_claim(self):
        context = self.env.context.copy()
        context.update({'default_workorder_id': self.id})
        return {
            'name': _("Claims"),
            'view_mode': 'tree,form',
            'res_model': 'crm.claim',
            'domain': [('id', 'in', self.claim_ids.ids)],
            'type': 'ir.actions.act_window',
            'context': context
        }

    def button_pending(self):
        self.ensure_one()
        super(MrpWorkorder, self).button_pending()
        wiz_obj = self.env['mrp.workorder.pending.wizard']
        wiz = wiz_obj.with_context({
            'active_id': self.id,
            'active_model': 'mrp.workorder'}).create({})
        context = self.env.context.copy()
        context.update({
            'active_id': self.id,
            'active_model': 'mrp.workorder'})
        return {'name': _('Pending Work Order'),
                'type': 'ir.actions.act_window',
                'res_model': 'mrp.workorder.pending.wizard',
                'view_type': 'form',
                'view_mode': 'form',
                'res_id': wiz.id,
                'target': 'new',
                'context': context}
