# Copyright 2022 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class CrmClaim(models.Model):
    _inherit = 'crm.claim'

    lot_id = fields.Many2one(
        string='Lot/Serial Number',
        comodel_name='stock.production.lot')
    type = fields.Selection(
        [('customer', 'Customer'),
         ('supplier', 'Supplier'),
         ('internal', 'Internal')],
        string='Type')
    contact_id = fields.Many2one(
        string='Contact',
        comodel_name='res.partner')
    immediate_action = fields.Text(
        string='Immediate Action')
