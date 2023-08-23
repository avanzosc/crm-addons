# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Claims Usability",
    "version": "16.0.1.0.0",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/crm-addons",
    "depends": [
        "base",
        "crm_claim",
    ],
    "data": [
        "security/crm_claim_usability_groups.xml",
        "data/crm_claim_usability_data.xml",
        "views/crm_claim_view.xml",
        "views/res_config_settings_view.xml",
        "views/res_partner_view.xml",
    ],
    "installable": True,
}
