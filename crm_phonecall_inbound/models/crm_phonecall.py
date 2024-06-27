# Copyright 2021 Berezi - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models


class CrmPhonecall(models.Model):
    _inherit = "crm.phonecall"

    phonecall_time_ids = fields.One2many(
        string="Phone calls",
        comodel_name="crm.phonecall.time",
        inverse_name="phonecall_id",
    )
    show_init_call = fields.Boolean(
        string="Show init call button",
        compute="_compute_show_init_call",
    )
    direction = fields.Selection(default="in")
    commercial_partner_id = fields.Many2one(
        string="Commercial partner",
        comodel_name="res.partner",
        related="partner_id.commercial_partner_id",
        store=True,
    )

    @api.onchange("partner_phone")
    def onchange_partner_phone_id(self):
        if self.partner_phone:
            cond = [
                "|",
                ("phone", "=", self.partner_phone),
                ("mobile", "=", self.partner_phone),
            ]
            partners = self.env["res.partner"].search(cond)
            if len(partners) == 1:
                self.partner_id = partners.id
            if len(partners) > 1:
                self.commercial_partner_id = partners[0].commercial_partner_id.id

    def _compute_show_init_call(self):
        for inbound in self:
            if not inbound.phonecall_time_ids:
                inbound.show_init_call = True
            else:
                found = inbound.phonecall_time_ids.filtered(lambda x: not x.date_closed)
                if found:
                    inbound.show_init_call = False
                else:
                    inbound.show_init_call = True

    def action_button_initiate_call(self):
        initiate_call_vals = {
            "phonecall_id": self.id,
            "date_open": fields.Datetime.now(),
            "duration": "0:00:00",
            "team_id": self.user_id.team_id.id,
        }
        return self.env["crm.phonecall.time"].create(initiate_call_vals)

    def action_button_end_call(self):
        line = self.phonecall_time_ids.filtered(lambda x: not x.date_closed)
        if line:
            line.write({"date_closed": fields.Datetime.now()})
        self.state = "done"
