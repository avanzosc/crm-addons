# Copyright 2021 Berezi - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class CrmPhonecallTransfer(models.TransientModel):
    _name = "crm.phonecall.transfer"
    _description = "Wizard to transfer phone call"

    phonecall_id = fields.Many2one(
        string="Phone call",
        comodel_name="crm.phonecall",
    )
    user_id = fields.Many2one(
        string="Commercial",
        comodel_name="res.users",
    )
    team_id = fields.Many2one(
        string="Sales team",
        comodel_name="crm.team",
        default=lambda self: self.user_id.team_id,
    )

    @api.model
    def default_get(self, fields_list):
        res = super(CrmPhonecallTransfer, self).default_get(fields_list)
        if self.env.context.get("active_model") == "crm.phonecall":
            res.update(
                {
                    "phonecall_id": self.env.context.get("active_id"),
                }
            )
        return res

    def button_generate_transfer(self):
        if self.user_id or self.team_id:
            self.phonecall_id.action_button_end_call()
            new_line = self.phonecall_id.action_button_initiate_call()
            new_line.update(
                {
                    "user_id": self.user_id.id,
                    "team_id": self.team_id.id,
                }
            )
            self.phonecall_id.update(
                {
                    "state": "pending",
                }
            )
