from odoo import fields, models


class PCB(models.Model):
    _name = "pcb.pcb"
    _description = "PCB"

    name = fields.Char(string="Nombre", required=True)


class CrmClaim(models.Model):
    _inherit = "crm.claim"

    pcb_id = fields.Many2one("pcb.pcb", string="PCB")
