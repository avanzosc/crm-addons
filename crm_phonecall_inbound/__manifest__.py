# Copyright 2021 Berezi - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM Phonecall Inbound",
    "version": "14.0.1.0.0",
    "author": "Avanzosc",
    "website": "https://github.com/avanzosc/crm-addons",
    "category": "Sales/CRM",
    "depends": [
        "crm_phonecall",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/crm_phonecall_transfer_view.xml",
        "views/crm_phonecall_views.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
}
