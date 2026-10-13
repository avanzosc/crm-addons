# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM Claim Stock Picking Create Repair",
    "version": "18.0.1.0.0",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/crm-addons",
    "depends": ["crm_claim", "stock_picking_create_repair"],
    "data": [
        "views/crm_claim_views.xml",
        "views/sale_order_views.xml",
        "views/stock_picking_views.xml",
        "views/repair_order_views.xml",
        "views/account_move_views.xml",
    ],
    "installable": True,
}
