# Copyright 2019 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "CRM Claim Analytic",
    "version": "12.0.1.0.0",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "depends": [
        "crm_claim",
        "analytic",
    ],
    "data": [
        "views/account_analytic_account_view.xml",
        "views/account_analytic_line_view.xml",
        "views/crm_claim_view.xml",
    ],
    "installable": True,
}
