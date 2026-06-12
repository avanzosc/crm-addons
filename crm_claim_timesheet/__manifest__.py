# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Claim Timesheets",
    "version": "14.0.2.0.0",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/crm-addons",
    "depends": [
        "crm_claim",
        "crm_claim_usability",
        "hr_timesheet",
        "hr_timesheet_task_required",
    ],
    "excludes": [],
    "data": [
        "views/account_analytic_line_view.xml",
        "views/crm_claim_view.xml",
        "views/project_task_view.xml",
        "views/project_portal_templates.xml",
        "reports/report_project_task_templates.xml",
        "reports/report_timesheet_templates.xml",
    ],
    "installable": True,
}
