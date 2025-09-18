# Copyright 2025 Alfredo de Afuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Crm Claim Mrp Production Control",
    "version": "16.0.1.0.0",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/crm-addons",
    "depends": ["crm_claim", "mrp_production_control", "crm_claim_type"],
    "data": [
        "views/mrp_production_control_views.xml",
        "views/crm_claim_views.xml",
    ],
    "installable": True,
    "auto_install": True,
}
