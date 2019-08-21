# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "CRM Claim Timesheet",
    "version": "12.0.1.0.0",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "depends": [
        "crm_claim",
        "hr_timesheet"
    ],
    "data": [
        "views/crm_claim_view.xml",
        "views/hr_timesheet_view.xml",
    ],
    "installable": True,
}
