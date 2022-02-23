# Copyright 2022 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM Claim Non Conformity Report",
    'version': '14.0.1.0.0',
    "author": "Avanzosc",
    "category": "Sales/CRM",
    "website": "http://www.avanzosc.es",
    "depends": [
        "crm_claim_code",
        "stock",
    ],
    "data": [
        "report/claim_report.xml",
        "report/crm_report_template.xml",
        "views/crm_claim_views.xml",
        "views/res_users_views.xml",
    ],
    "license": "AGPL-3",
    'installable': True,
}
