# Copyright 2023 Berezi Amubieta - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM Lead Payment",
    "version": "14.0.1.0.0",
    "author": "Avanzosc",
    "website": "https://github.com/avanzosc/crm-addons",
    "category": "Sales/CRM",
    "depends": [
        "sale_crm",
        "account_payment_mode",
        "account_payment_partner",
    ],
    "data": [
        "views/crm_lead_view.xml",
        "views/sale_order_view.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
}
