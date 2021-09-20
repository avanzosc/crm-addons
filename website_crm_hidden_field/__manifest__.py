# Copyright 2021 Leire Martinez de Santos - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Website CRM hidden field',
    'category': 'Website',
    'sequence': 55,
    'summary': 'Hidden field in contactus.',
    "author": "AvanzOSC",
    'website': 'http://www.avanzosc.es/',
    'version': '1.0',
    'depends': [
        'website_crm',
    ],
    'data': [
        'views/templates.xml',
    ],
    'installable': True,
}
