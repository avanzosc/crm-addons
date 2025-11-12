# (c) 2015 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    amount_delivered = fields.Float(digits="Product Unit of Measure", default=0.0)
