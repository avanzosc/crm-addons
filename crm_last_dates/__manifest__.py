# Copyright 2025 Unai Beristain - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM Last Dates",
    "version": "18.0.1.0.0",
    "author": "Avanzosc",
    "summary": "Add last lead, meeting, and invoice dates to res.partner.",
    "website": "https://github.com/avanzosc/crm-addons",
    "license": "LGPL-3",
    "depends": ["crm", "calendar", "account"],
    "data": ["views/res_partner_view.xml"],
    "installable": True,
    "application": False,
}
