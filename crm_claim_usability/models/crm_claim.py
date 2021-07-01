# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    commercial_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Commercial Entity",
        related="partner_id.commercial_partner_id",
        store=True,
        index=True,
    )
    user_id = fields.Many2one(
        domain=lambda self: [
            ("groups_id", "in", self.env.ref("base.group_user").id)],
    )

    def name_get(self):
        result = []
        name_pattern = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("crm_claim_usability.display_name", default="")
        )
        origin = super().name_get()
        if self.env.context.get("no_display_code", False):
            return origin
        orig_name = dict(origin)
        for claim in self:
            name = orig_name[claim.id]
            try:
                code = claim.code
            except Exception:
                code = False
            if code and name_pattern:
                name = name_pattern % {"name": name, "code": code}
            result.append((claim.id, name))
        return result

    def with_user(self, user):
        """ with_user(user)

        Return a new version of this recordset attached to the given user, in
        non-superuser mode, unless `user` is the superuser (by convention, the
        superuser is always in superuser mode.)
        """
        if not user.has_group("base.group_user"):
            user = (self.env.user if self.env.user.has_group("base.group_user")
                    else self.env.ref("base.user_root"))
        return super(CrmClaim, self).with_user(user)
