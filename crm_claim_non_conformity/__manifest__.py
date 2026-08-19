# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM Claim Non Conformity",
    "version": "18.0.1.0.0",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/crm-addons",
    "depends": [
        "crm_claim_type_sequence",
        "crm_claim_department",
        "crm_claim_report",
        "crm_claim_code",
        "stock",
    ],
    "data": [
        "data/crm_claim_type.xml",
        "security/ir.model.access.csv",
        "views/crm_claim_type_views.xml",
        "views/crm_claim_views.xml",
        "views/res_users_views.xml",
        "report/crm_claim_non_conformity_report_view.xml",
        "report/crm_claim_report_document.xml",
        "report/crm_claim_layout.xml",
        "report/non_conformity_report.xml",
    ],
    "installable": True,
}
