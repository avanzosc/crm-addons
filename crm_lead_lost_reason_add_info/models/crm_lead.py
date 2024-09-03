from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    competitor_manufacturer_id = fields.Many2one(
        "res.partner",
        string="Competitor Manufacturer",
        domain=[("is_company", "=", True)],
    )
    competitor_integrator_id = fields.Many2one(
        "res.partner",
        string="Competitor Integrator",
        domain=[("is_company", "=", True)],
    )
    competitor_reseller_id = fields.Many2one(
        "res.partner",
        string="Competitor Reseller",
        domain=[("is_company", "=", True)],
    )
    competitor_price = fields.Float()
    lost_reason_notes = fields.Text()

    def action_mark_lost(self):
        """
        Extends the action to mark a lead as lost to include additional fields in the wizard.
        """
        res = super().action_mark_lost()
        return res
