==========================
CRM claim extra ref report
==========================

.. |badge1| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: https://www.gnu.org/licenses/agpl-3.0.en.html
    :alt: License: AGPL-3

|badge1|

This module bridges ``crm_claim_extra_ref`` and ``crm_claim_report``.
It extends the claim report template to include the extra references
(``Reference 2`` and ``Reference 3``) provided by ``crm_claim_extra_ref``.

This module is intentionally separated so that:

* ``crm_claim_extra_ref`` has no dependency on report modules.
* ``crm_claim_report`` has no dependency on extra reference modules.

**Table of contents**

.. contents::
   :local:

Usage
=====

Install this module only when both modules are installed:

* ``crm_claim_extra_ref``
* ``crm_claim_report``

After installation, the claim report will show ``Reference 2`` and
``Reference 3`` when those values exist on the claim.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/avanzosc/crm-addons/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/avanzosc/crm-addons/issues/new?body=module:%20crm_claim_extra_ref_report%0Aversion:%2018.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* AvanzOSC

Contributors
~~~~~~~~~~~~

* Ana Juaristi <anajuaristi@avanzosc.es>
* Eñaut Alberdi <enautavanzosc@gmail.com>

