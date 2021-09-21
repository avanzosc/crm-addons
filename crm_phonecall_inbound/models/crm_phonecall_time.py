# Copyright 2021 Berezi - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class CrmPhonecallTime(models.Model):
    _name = 'crm.phonecall.time'
    _description = 'Phone call times'

    phonecall_id = fields.Many2one(
        string='Inbound phone call', comodel_name='crm.phonecall')
    date_open = fields.Datetime(string="Call initiate date", readonly=True)
    duration = fields.Char(
        string='Duration', help="Duration in minutes and seconds.",
        compute='_compute_duration')
    date_closed = fields.Datetime(string="Call end date", readonly=True)
    user_id = fields.Many2one(
        string='Commercial', comodel_name='res.users',
        default=lambda self: self.env.user)
    team_id = fields.Many2one(
        string='Sales team', comodel_name='crm.team',
        default=lambda self: self.env.user.team_id)

    def _compute_duration(self):
        for line in self.filtered(lambda x: x.date_open):
            if not line.date_closed:
                line.duration = '00:00:00'
            else:
                hours = 0
                minutes = 0
                my_date = line.date_closed - line.date_open
                seconds = my_date.total_seconds()
                if seconds > 3600:
                    hours = divmod(seconds, 3600)[0]
                if hours > 0:
                    seconds = seconds - (hours * 3600)
                if seconds > 60:
                    minutes = divmod(seconds, 60)[0]
                if minutes > 0:
                    seconds = seconds - (minutes * 60)
                hours = str(int(hours)).zfill(2)
                minutes = str(int(minutes)).zfill(2)
                seconds = str(int(seconds)).zfill(2)
                line.duration = '{}:{}:{}'.format(hours, minutes, seconds)
