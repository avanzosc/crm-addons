.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=======================
Claims Management Close
=======================

Summary
-------
This module enables closing and opening claims, by defining a check in the
stages, marking them as closed.You can have separate menus for open and closed
claims.


Key Features
------------
- New checkbox **closed** on Claim stages.
- Visible in **form** view.

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
1. Go to ** CRM → Configuration → Settings → Claims Closure** and enable **Separated Claim Menus** checkbox.
2. Go to ** CRM → Configuration → Claim → stages** and enable **Closed** checkbox to indicate that the state closes the claim.


Technical Notes
---------------
- Model inheritance: ``crm.claim.state`` adds ``closed = fields.Boolean()``.
- View customizations in crm.claim.state:
  - Adds ``closed`` after ``sequence`` in the form view.
- Model Inheritance:  ``res.config.settings`` adds ``group_crm_claim_close = fields.Boolean(string="Separated Claim Menus", implied_group="crm_claim_close.group_crm_claim_close")``.
- View customizations in res.config.settings:
  - Adds ``group_crm_claim_close`` inside ``CRM - Configuration - Settings`` in the form view.
- View customizations in crm claim:
  - Adds ``Open Claims, Closed Claims, Closed Today, Closed Last Week, Closed Last Month, Closed Last Year, Date Closed`` after ``user_id`` in the search view.

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

Do not contact contributors directly about support or help with technical issues.
