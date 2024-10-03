from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    sequence = fields.Char(string="Opportunity Sequence", readonly=True, copy=False,)

    @api.model
    def create(self, vals):
        if 'sequence' not in vals or not vals['sequence']:
            vals['sequence'] = self.env['ir.sequence'].next_by_code('crm.lead.sequence') or '/'
        lead = super(CrmLead, self).create(vals)
        return lead
