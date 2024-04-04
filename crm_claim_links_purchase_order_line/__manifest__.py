# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM claim Links Purchase Order Line",
    "version": "16.0.1.0.0",
    "author": "AvanzOSC",
    "category": "Supplier Relationship Management",
    "license": "AGPL-3",
    "website": "http://www.avanzosc.es",
    "depends": [
        "crm_claim_links",
        "purchase_stock",
    ],
    "data": [
        "views/purchase_order_line_view.xml",
        "views/purchase_order_view.xml",
    ],
    "installable": True,
}
