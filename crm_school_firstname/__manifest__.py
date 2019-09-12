# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "CRM School Firstname",
    "version": "12.0.1.1.0",
    "category": "Hidden",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "depends": [
        "crm_school",
        "crm_lead_firstname",
    ],
    "data": [
        "views/crm_lead_future_student_view.xml",
        "views/crm_lead_view.xml",
    ],
    "installable": True,
    "auto_install": True,
}
