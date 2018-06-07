# -*- coding: utf-8 -*-
# Copyright 2015 Esther Martín - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import api, models


class CrmClaim(models.Model):
    _inherit = 'crm.claim'

    @api.multi
    def claim_re_open(self):
        for claim in self.filtered('date_closed'):
            claim.date_closed = False
            claim.stage_id = claim._get_default_stage_id()

    @api.multi
    def claim_close(self):
        for claim in self.filtered(lambda c: not c.date_closed):
            claim.date_closed = claim.write_date
