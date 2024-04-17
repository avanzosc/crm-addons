# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM Claim Tags",
    "version": "16.0.1.0.0",
    "author": "AvanzOSC",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "website": "http://www.avanzosc.es",
    "depends": [
        "crm_claim",
        "sales_team"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/crm_claim_tag_view.xml",
        "views/crm_claim_view.xml",
    ],
    "installable": True,
}
