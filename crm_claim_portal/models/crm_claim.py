# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models
from odoo.osv import expression


class CrmClaim(models.Model):
    _name = "crm.claim"
    _inherit = ["crm.claim", "portal.mixin"]

    def _compute_access_url(self):
        super()._compute_access_url()
        for task in self:
            task.access_url = "/my/claim/%s" % task.id

    def preview_crm_claim(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_url",
            "target": "self",
            "url": self.get_portal_url(),
        }

    @api.model
    def _name_search(
        self, name, args=None, operator="ilike", limit=100, name_get_uid=None
    ):
        args = args or []
        domain = []
        if name:
            domain = ["|", ("name", operator, name), ("code", operator, name)]
        return self._search(
            expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid
        )
