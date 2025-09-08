.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

================
Claims Usability
================

Summary
-------
Module that improves usability in claims.

* Added commercial entity in order to group by company.
* Only internal users can be responsible of a claim.
* Button box in claims form.

If crm_claim_code module is installed then display name will show the code.
How is it shown is configurable by parameters, and avoidable with a context
parameter.


Key Features
------------
- New fields **Commercial Entity** on Claims.
- Invisible in **form and List** view.
- New domain in **User** on Claims


Installation
------------
1. Copy the module directory into your Odoo ``addons`` path (e.g. ``/odoo/custom/addons``).
2. Update the Apps list and install the module from **Apps**.
   Alternatively, from the command line you can update the module:
   ::
     
     ./odoo-bin -d <your_db> -u <module_name>

Dependencies
------------
- crm_claim

Configuration & Usage
---------------------
1. Go to ** SETTINGS → Technical → Parameters → System Parameters → crm_claim_usability.display_name ** To define how the claim name will be displayed.
2. Go to ** CRM → Configuration → Settings → Claims Usability** and enable **Show Metadata Info in Claims** checkbox.
3. Go to ** SETTINGS → Users&Companies → groups → Metadata Info on Claims ** To define users to view write date.


Technical Notes
---------------
- Model inheritance: ``crm.claim`` adds ``commercial_partner_id = fields.Many2one(comodel_name="res.partner", string="Commercial Entity", related="partner_id.commercial_partner_id", store=True, index=True)``.
- Model inheritance: ``crm.claim`` adds ``user_id = fields.Many2one(domain=lambda self: [("groups_id", "in", self.env.ref("base.group_user").id)],)``.
- View customizations in crm.claim:
  - Adds ``commercial_partner_id`` after ``partner_id`` in the form and list view, as invisible.
- Model Inheritance:  ``res.config.settings`` adds ``group_crm_claim_technical = fields.Boolean(string="Show Metadata Info in Claims", implied_group="crm_claim_usability.group_crm_claim_technical",)``.
- View customizations in res.config.settings:
  - Adds ``group_crm_claim_technical`` inside ``CRM - Configuration - Settings`` in the form view.
- Model Inheritance:  ``ir.config_parameter`` adds key ``crm_claim_usability.display_name``.
- View customizations in ir.config_parameter:
  - Adds key ``crm_claim_usability.display_name`` inside ``Settings - Technical - Parameters - System Parameters`` in the tree view.
- View customizations in crm claim:
  - Adds Filters ``Unassigned Claims, My Claims, Today, Last Week, Last Month, Last Year, Date`` after ``user_id`` in the search view.
  - Adds Filters ``Commercial Entity, Write Date`` after ``partner`` in the search view.



Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/avanzosc/crm-addons/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Contributors
------------
* Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>
* Ana Juaristi <ajuaristio@gmail.com>

Do not contact contributors directly about support or help with technical issues.
