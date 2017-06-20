# -*- coding: utf-8 -*-
# Copyright © 2017 Oihane Crucelaegui - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Contact Form with Customer Payment",
    "summary": "Customer payment info in contact form",
    "version": "8.0.1.0.0",
    "category": "Website",
    "license": "AGPL-3",
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "contributors": [
        "Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>",
        "Ana Juaristi <anajuaristi@avanzosc.es>",
    ],
    "depends": [
        "website_crm",
        "crm_lead_customer_payment",
    ],
    "data": [
        "views/contactus_form.xml",
    ],
    "installable": True,
    "auto-install": True,
}
