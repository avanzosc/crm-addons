# Copyright 2025 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Crm Claim Sale Repair Cost",
    "version": "18.0.1.0.0",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/crm-addons",
    "category": "Customer Relationship Management",
    "depends": [
        "crm_claim_extra_ref",
        "stock_picking_create_repair",
        "sale_line_pending_info",
        "sale_stock_move_cost",
    ],
    "data": [
        "views/crm_claim_views.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
}
