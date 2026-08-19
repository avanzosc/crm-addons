# Copyright 2024 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Crm Claim Department",
    "version": "18.0.1.0.0",
    "author": "AvanzOSC",
    "website": "https://github.com/avanzosc/crm-addons",
    "category": "Customer Relationship Management",
    "depends": ["crm_claim", "crm_claim_usability", "hr"],
    "data": [
        "reports/crm_claim_report_view.xml",
        "views/crm_claim_views.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
    "post_init_hook": "_post_install_put_department_in_claims",
}
