# -*- coding: utf-8 -*-
# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CrmConfiguration(models.TransientModel):
    _inherit = 'sale.config.settings'

    module_crm_lead_show_action = fields.Boolean(
        string="Show Lead Actions",
        help='Allows you to see which actions are going to take and when.\n'
             '-This installs the module crm_lead_show_action.')
