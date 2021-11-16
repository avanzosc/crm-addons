# Copyright 2021 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM Claim Stock Picking",
    'version': '14.0.1.0.0',
    "author": "Avanzosc",
    "category": "Sales/CRM",
    "depends": [
        "stock",
        "crm_claim",
        "crm_claim_usability"
    ],
    "data": [
        "views/stock_picking_views.xml",
        "views/crm_claim_views.xml",
    ],
    "license": "AGPL-3",
    'installable': True,
}
