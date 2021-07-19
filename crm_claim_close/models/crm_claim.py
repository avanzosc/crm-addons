# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    def action_close(self):
        for record in self.filtered(lambda c: not c.date_closed):
            record.date_closed = fields.Datetime.now()

    def action_open(self):
        for record in self.filtered("date_closed"):
            record.date_closed = False

    @api.model
    def create(self, values):
        if "stage_id" in values:
            stage = self.env["crm.claim.stage"].browse(values.get("stage_id"))
            if stage.closed:
                values["date_closed"] = fields.Datetime.now()
        return super(CrmClaim, self).create(values)

    def write(self, values):
        result = super(CrmClaim, self).write(values)
        if "stage_id" in values:
            stage = self.env["crm.claim.stage"].browse(values.get("stage_id"))
            if stage.closed:
                self.action_close()
            else:
                self.action_open()
        return result
