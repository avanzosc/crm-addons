# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models


class CrmClaim(models.Model):
    _name = "crm.claim"
    _inherit = ["crm.claim", "portal.mixin", "rating.mixin"]

    def _compute_access_url(self):
        super(CrmClaim, self)._compute_access_url()
        for task in self:
            task.access_url = '/my/claim/%s' % task.id
