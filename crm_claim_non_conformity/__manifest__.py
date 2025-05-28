# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM Claim Non Conformity",
    "version": "16.0.1.0.0",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/crm-addons",
    "depends": ["crm_claim_type_sequence", "crm_claim_department"],
    "data": [
        "security/ir.model.access.csv",
        "views/crm_claim_type_views.xml",
        "views/crm_claim_views.xml",
        "report/crm_claim_non_conformity_report_view.xml",
    ],
    "installable": True,
}
