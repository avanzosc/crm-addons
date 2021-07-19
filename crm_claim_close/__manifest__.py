# Copyright 2021 Oihane Crucelaegui - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Claims Management Close",
    "version": "14.0.1.0.0",
    "category": "Customer Relationship Management",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "depends": [
        "crm_claim",
    ],
    "data": [
        "data/crm_claim_data.xml",
        "security/crm_claim_close_groups.xml",
        "views/crm_claim_view.xml",
        "views/crm_claim_stage_view.xml",
        "views/crm_claim_close_menu.xml",
        "views/res_config_settings_view.xml",
    ],
    "installable": True,
    "post_init_hook": "post_init_hook",
}
