.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

================
CRM Claim Portal
================

Summary
-------
This module allows portal user access to their related claims.


Key Features
------------
- New button **preview_crm_claim** on Claims.
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
- crm_claim, crm_claim_code, crm_claim_usability and portal.


Technical Notes
---------------
- Model inheritance: ``crm.claim`` adds function ``preview_crm_claim``.
- View customizations in crm.claim:
  - Add button ``Preview Claim`` inside ``header`` in the form view
- View customizations in crm.claim:
  - Add button ``Preview Claim`` inside ``header`` in the form view
- Model inheritance: ``ir.rule`` new rule ``Claim Portal``.
- Portal view customizations to show claims.


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
