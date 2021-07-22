# Copyright 2021 Daniel Campos - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "CRM Claim Corrective",
    "version": "14.0.1.0.0",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "https://www.avanzosc.es",
    "summary": "Extends CRM Claims with corrective actions",
    "depends": [
        "crm_claim",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/crm_claim_corrective_sequence.xml",
        "views/crm_claim_corrective_view.xml",
        "views/crm_claim_view.xml",
        "views/crm_claim_menu.xml",
    ],
    "installable": True,
}
