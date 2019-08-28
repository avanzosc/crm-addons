# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def catch_new_student_vals(self, future_student):
        partner_dict = super(CrmLead, self).catch_new_student_vals(
            future_student)
        if future_student.name:
            partner_dict.update({
                'firstname': future_student.name,
            })
            if 'name' in partner_dict:
                del partner_dict['name']
        if future_student.lastname:
            partner_dict.update({
                'lastname': future_student.lastname,
            })
        return partner_dict
