# Copyright 2019 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "CRM School",
    "version": "12.0.2.1.0",
    "license": "AGPL-3",
    "depends": [
        "crm",
        "crm_lead_vat",
        "contacts_school",
        "sales_team",
        "partner_contact_birthdate",
        "partner_contact_gender",
        "education",
    ],
    "author": "AvanzOSC",
    "website": "http://www.avanzosc.es",
    "category": "Sales",
    "data": [
        "security/ir.model.access.csv",
        "views/crm_lead_future_student_view.xml",
        "views/crm_lead_view.xml",
        "views/crm_team_view.xml",
        "views/res_partner_view.xml",
        "wizard/crm_lead_to_opportunity_views.xml",
    ],
    "installable": True,
}
