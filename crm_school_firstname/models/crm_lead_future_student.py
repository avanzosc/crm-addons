# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CrmLeadFutureStudent(models.Model):
    _inherit = 'crm.lead.future.student'

    name = fields.Char(string='First name')
    lastname = fields.Char(string='Last name')

    @api.onchange('child_id')
    def onchange_child_id(self):
        super(CrmLeadFutureStudent, self).onchange_child_id()
        if self.child_id:
            self.name = self.child_id.firstname
            self.lastname = self.child_id.lastname
