# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import tools
from odoo import api, fields, models
from psycopg2.extensions import AsIs


class FutureStudentProgenitorReport(models.Model):
    _name = "future.student.progenitor.report"
    _description = "Future Student Progenitor List"
    _auto = False
    _rec_name = "student_id"
    _order = "academic_year_id desc,center_id,course_id,student_id," \
             "progenitor_id"

    academic_year_id = fields.Many2one(
        comodel_name="education.academic_year", string="Academic Year")
    center_id = fields.Many2one(
        comodel_name="res.partner", string="Education Center")
    course_id = fields.Many2one(
        comodel_name="education.course", string="Education Course")
    student_id = fields.Many2one(
        comodel_name="res.partner", string="Future Student")
    student_email = fields.Char()
    student_phone = fields.Char()
    student_mobile = fields.Char()
    progenitor_id = fields.Many2one(
        comodel_name="res.partner", string="Progenitor")
    progenitor_email = fields.Char()
    progenitor_phone = fields.Char()
    progenitor_mobile = fields.Char()

    _depends = {
        "crm.lead.future.student": [
            "academic_year_id", "school_id", "course_id", "child_id",
        ],
        "res.partner": [
            "student_progenitor_ids", "email", "phone", "mobile",
        ],
    }

    def _select(self):
        select_str = """
            SELECT
                row_number() OVER () as id,
                future_student.academic_year_id as academic_year_id,
                future_student.school_id as center_id,
                future_student.course_id as course_id,
                stu.id as student_id,
                stu.email as student_email,
                stu.phone as student_phone,
                stu.mobile as student_mobile,
                pro.id as progenitor_id,
                pro.email as progenitor_email,
                pro.phone as progenitor_phone,
                pro.mobile as progenitor_mobile
        """
        return select_str

    def _from(self):
        from_str = """
                FROM crm_lead_future_student future_student
                JOIN res_partner stu ON future_student.child_id = stu.id
                JOIN rel_student_progenitor rel
                  ON rel.student_id = stu.id
                JOIN res_partner pro ON rel.progenitor_id = pro.id
        """
        return from_str

    def _group_by(self):
        group_by_str = """
            GROUP BY
                future_student.academic_year_id,
                future_student.school_id,
                future_student.course_id,
                stu.id,
                stu.email,
                stu.phone,
                stu.mobile,
                pro.id,
                pro.email,
                pro.phone,
                pro.mobile
        """
        return group_by_str

    @api.model_cr
    def init(self):
        # self._table = education_group_student_progenitor_report
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute(
            """CREATE or REPLACE VIEW %s as
                (
                %s %s %s
            )""", (
                AsIs(self._table), AsIs(self._select()), AsIs(self._from()),
                AsIs(self._group_by()),))
