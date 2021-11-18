# Copyright 2021 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class MrpWorkorderPendingWizard(models.TransientModel):
    _name = "mrp.workorder.pending.wizard"
    _description = "Wizard to create a claim"

    create_claim = fields.Boolean(string='Create Claim')
    loss_id = fields.Many2one(
        string='Problem Description',
        comodel_name='mrp.workcenter.productivity.loss')

    def name_get(self):
        result = []
        workorder = self.env['mrp.workorder'].browse(
                self.env.context.get('active_id'))
        name = u'{} {} {} {}'.format(
            workorder.production_id.name, workorder.name,
            workorder.product_id.name, self.loss_id.name)
        result.append((workorder.id, name))
        return result

    def button_create_claim(self):
        if self.create_claim:
            workorder = self.env['mrp.workorder'].browse(
                self.env.context.get('active_id'))
            claim_vals = {'workorder_id': workorder.id,
                          'production_id': workorder.production_id.id,
                          'user_id': self.env.user.id,
                          'name': self.name_get()[0][1],
                          'loss_id': self.loss_id.id}
            self.env['crm.claim'].create(claim_vals)
        else:
            return False
