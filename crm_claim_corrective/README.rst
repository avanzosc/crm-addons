====================
CRM Claim Corrective
====================

.. |badge1| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge1|

This module extends CRM Claims so that, once the root cause of a claim is
known, a **corrective action plan** can be created from the claim and
followed up until it is closed. It also adds reusable **description
templates** to fill in the claim texts quickly, and an **Images** tab to
attach up to four photos to each claim.

**Table of contents**

.. contents::
   :local:

Features
========

Corrective action plans
~~~~~~~~~~~~~~~~~~~~~~~

A corrective action plan (``crm.claim.corrective``) is linked to one claim
and contains:

* **Sequence**: automatic reference with the ``AACC`` prefix
  (``AACC00001``, ``AACC00002``...).
* **Claim** and **Customer**: the claim it comes from and its partner,
  both filled in automatically and read-only.
* **Status**: *Draft*, *Pending* or *Closed*. The status bar can be
  clicked to move the plan from one status to another.
* **Corrective actions**: the list of tasks to carry out. Each one has a
  description, a **Responsible** user, a **Planned Date** and a
  **Date Done**. Rows can be reordered by dragging them.

Description templates
~~~~~~~~~~~~~~~~~~~~~

Claims that repeat over time usually have the same description, cause and
resolution texts. Instead of typing them every time, they can be saved as
templates of three types:

* **Claim Description**: fills in the claim description.
* **Cause Description**: fills in the root cause.
* **Resolution Description**: fills in the resolution actions.

When a template is selected on a claim, its text is copied into the
matching field, where it can still be edited freely. Each selector only
offers templates of its own type.

Claim photos
~~~~~~~~~~~~

A new **Images** tab on the claim form holds up to four photos (for
example, of the damaged product). They are stored as attachments.

Reports
~~~~~~~

* **Corrective action** (new): PDF with the plan reference, claim,
  customer and the table of corrective actions (responsible, planned date
  and date done). It is printed in the customer's language.
* **Claim report** (from ``crm_claim_report``, extended): the name of the
  selected template is printed in front of the description, cause and
  resolution texts, and the claim photos are printed after the main
  section, two per row.

Configuration
=============

Access rights
~~~~~~~~~~~~~

* **Internal users** can see claim description templates and corrective action
  plans, but cannot change them.
* **Sales / User: Own Documents Only** and above can create, edit and
  delete descriptions, plans and corrective actions.
* The **Corrective action** PDF report can only be printed by
  **Sales / Administrator**.

Templates
~~~~~~~~~

#. Activate the developer mode (the menu is only visible in this mode).
#. Go to *CRM > Configuration > Claim > Descriptions*.
#. Create one record per template, filling in:

   * **Name**: short title. It is what users see in the selector and
     what is printed in the claim report.
   * **Description**: the full text that will be copied into the claim.
   * **Description Type**: *Claim Description*, *Cause Description* or
     *Resolution Description*.

Templates can also be created on the fly from the claim form: the type is
set automatically depending on the selector used.

Sequence
~~~~~~~~

The ``AACC`` prefix and the 5-digit padding come from the
*Corrective Action* sequence (*Settings > Technical > Sequences &
Identifiers > Sequences*, developer mode). It can be changed there and
will not be overwritten when the module is updated.

Usage
=====

Filling in a claim
~~~~~~~~~~~~~~~~~~

#. Go to *CRM > After Sale > Claims* and open or create a claim.
#. On the **Claim Description** tab, select a template in
   **Claim Description** to fill in the description text.
#. On the **Follow Up** tab:

   * Select a template in **Cause Description** to fill in the root cause.
   * Select a template in **Resolution Description** to fill in the
     resolution actions.

#. On the **Images** tab, upload up to four photos.

Creating a corrective action plan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. On the **Follow Up** tab of the claim, fill in the root cause.
#. Click **Create Corrective Action**. The button only appears when the
   root cause is filled in and the claim has no plan yet.
#. A new plan is created in *Draft* status and linked to the claim. The
   **Claim Corrective** field (next to the action type) shows it; click
   on it to open the plan.

Following up the plan
~~~~~~~~~~~~~~~~~~~~~

#. Open the plan from the claim, or from *CRM > After Sale > Corrective
   Actions*, where all plans are listed with their claim, customer and
   status.
#. Add one line per task in **Corrective Actions**, with its responsible
   user and planned date. Drag the rows to set their order.
#. Move the plan to *Pending* while the actions are being carried out,
   and fill in the **Date Done** of each action as it is finished.
#. When everything is done, set the plan to *Closed*.
#. To share the plan, use *Print > Corrective action*.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/avanzosc/crm-addons/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smash it by providing a detailed and welcomed
`feedback <https://github.com/avanzosc/crm-addons/issues/new?body=module:%20crm_claim_corrective%0Aversion:%2018.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* AvanzOSC

Contributors
~~~~~~~~~~~~

* Ana Juaristi <anajuaristi@avanzosc.es>
* Daniel Campos <danielcampos@avanzosc.es>
* Lucía Echeverría <luciaecheverria@avanzosc.es>
