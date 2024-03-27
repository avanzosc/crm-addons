# -*- coding: utf-8 -*-
# Copyright Ainara Galdona - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Crm Claim Report",
    'version': '8.0.1.0.0',
    'license': "AGPL-3",
    'author': "AvanzOSC",
    'website': "http://www.avanzosc.es",
    'contributors': [
        "Ainara Galdona <ainaragaldona@avanzosc.es",
    ],
    "category": "Customer Relationship Management",
    "depends": [
        'crm_claim',
        'crm_claim_code',
        'crm_claim_type',
    ],
    "data": [
        'views/crm_claim_report_document.xml',
        'views/crm_claim_report.xml',
    ],
    "installable": True,
}
