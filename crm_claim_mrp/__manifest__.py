# Copyright 2021 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM Claim MRP",
    "version": "14.0.2.0.0",
    "author": "Avanzosc",
    "website": "https://github.com/avanzosc/crm-addons",
    "category": "Sales/CRM",
    "depends": [
        "mrp",
        "crm_claim",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/mrp_workorder_views.xml",
        "views/mrp_production_views.xml",
        "views/crm_claim_views.xml",
        "wizard/mrp_workorder_pending_wizard_views.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
}
