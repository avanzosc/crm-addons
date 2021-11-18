# Copyright 2021 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields, api


class CrmClaim(models.Model):
    _inherit = 'crm.claim'

    workorder_id = fields.Many2one(
        string='Work Order', comodel_name='mrp.workorder')
    production_id = fields.Many2one(
        string='Production', comodel_name='mrp.production')
    loss_id = fields.Many2one(
        string='Problem Description',
        comodel_name='mrp.workcenter.productivity.loss')

    @api.onchange('workorder_id')
    def onchange_production_id(self):
        if self.workorder_id:
            self.production_id = self.workorder_id.production_id

    @api.onchange('production_id')
    def onchange_workorder_id(self):
        self.ensure_one()
        domain = []
        if self.production_id:
            domain = ['|', ('production_id', '=', self.production_id.id), (
                'production_id', '=', False)]
        return {'domain': {'workorder_id': domain}}
