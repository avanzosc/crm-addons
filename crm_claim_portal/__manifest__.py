# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "CRM Claim Portal",
    "version": "14.0.1.0.0",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "depends": [
        "crm_claim",
        "crm_claim_usability",
        "portal",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/crm_claim_security.xml",
        "views/crm_claim_template.xml",
        "views/crm_claim_view.xml",
    ],
    "installable": True,
}
