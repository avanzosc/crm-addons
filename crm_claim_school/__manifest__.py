# Copyright 2019 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "CRM Claim School",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        "fetchmail",
        "crm_claim",
        "contacts_school",
        "crm_school",
    ],
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "category": "Customer Relationship Management",
    "data": [
        "security/ir.model.access.csv",
        "views/crm_claim_category_view.xml",
        "views/fetchmail_server_view.xml",
        "views/crm_claim_school_menu.xml",
    ],
    "installable": True,
}
