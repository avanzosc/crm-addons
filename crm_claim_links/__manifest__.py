# Copyright 2008 Daniel (Avanzosc) <danielcampos@avanzosc>
# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM claim Links",
    "version": "16.0.1.0.0",
    "author": "OdooMRP team,"
              "AvanzOSC,"
              "Serv. Tecnol. Avanzados - Pedro M. Baeza",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "website": "http://www.avanzosc.es",
    "description": """
    This module adds:

    - A link to crm claims in the stock pickings
    - A link to crm claims in repair orders
    - A Field for Supplier Stock Picking Reference in stock picking Receipts
    - For each crm claim, its associated Stock Pickings and repair orders list
    - For any product return it must have a crm claim linked.
    """,
    "depends": [
        "crm_claim",
        "repair",
        "stock"
    ],
    "data": [
        "views/stock_picking_view.xml",
        "views/stock_move_view.xml",
        "views/res_partner_view.xml",
        "views/repair_order_view.xml",
        "views/crm_claim_view.xml"
    ],
    "installable": True,
}
