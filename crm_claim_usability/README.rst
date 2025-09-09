.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

================
Claims Usability
================
Module that improves usability in claims.

* Added commercial entity in order to group by company.
* Only internal users can be responsible of a claim.
* Button box in claims form.

If crm_claim_code module is installed then display name will show the code.
How is it shown is configurable by parameters, and avoidable with a context
parameter.

Key Features
============
- New fields **Commercial Entity** on Claims.
- Invisible in **form and List** view.
- New domain in **User** on Claims

Configuration
=============
1. Go to ** SETTINGS → Technical → Parameters → System Parameters → crm_claim_usability.display_name ** To define how the claim name will be displayed.
2. Go to ** CRM → Configuration → Settings → Claims Usability** and enable **Show Metadata Info in Claims** checkbox.
3. Go to ** SETTINGS → Users&Companies → groups → Metadata Info on Claims ** To define users to view write date.

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
