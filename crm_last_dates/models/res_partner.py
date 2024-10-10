from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    last_lead_date = fields.Datetime(
        compute="_compute_last_lead_date",
        store=True,
    )
    last_meeting_date = fields.Datetime(
        compute="_compute_last_meeting_date",
        store=True,
    )
    last_invoice_date = fields.Datetime(
        compute="_compute_last_invoice_date",
        store=True,
    )

    @api.depends("commercial_partner_id", "opportunity_ids", "child_ids")
    def _compute_last_lead_date(self):
        for partner in self:
            lead_dates = partner.mapped("opportunity_ids.create_date") + partner.mapped(
                "child_ids.opportunity_ids.create_date"
            )
            partner.last_lead_date = max(lead_dates) if lead_dates else False

    @api.depends("commercial_partner_id", "meeting_ids", "child_ids")
    def _compute_last_meeting_date(self):
        for partner in self:
            meeting_dates = partner.mapped("meeting_ids.create_date") + partner.mapped(
                "child_ids.meeting_ids.create_date"
            )
            partner.last_meeting_date = max(meeting_dates) if meeting_dates else False

    @api.depends("commercial_partner_id", "invoice_ids", "child_ids")
    def _compute_last_invoice_date(self):
        for partner in self:
            invoice_dates = partner.mapped("invoice_ids.create_date") + partner.mapped(
                "child_ids.invoice_ids.create_date"
            )
            partner.last_invoice_date = max(invoice_dates) if invoice_dates else False
