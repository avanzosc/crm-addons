# (c) 2015 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    claim_closing_days = fields.Integer(string="Claim closing days")
