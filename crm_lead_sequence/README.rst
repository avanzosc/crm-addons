.. image:: https://img.shields.io/badge/license-LGPL--3-blue.svg
   :target: https://opensource.org/licenses/LGPL-3.0
   :alt: License: LGPL-3

=========================
CRM Lead Sequence
=========================

Overview
========

The **CRM Lead Sequence** module adds a unique sequence number to CRM opportunities in Odoo, allowing for easy identification and tracking of leads.

Features
========

- **Automatic Sequence Generation**: Automatically assigns a unique sequence to each CRM opportunity upon creation.
- **Sequence Field in Views**: The sequence number is displayed in the Kanban, Form and List views for CRM opportunities.

Usage
=====

1. **Install the Module**:

   - Install the module through the Odoo apps interface or place it in your Odoo addons directory.

2. **Creating an Opportunity**:

   - When a new CRM opportunity is created, the module will automatically assign a unique sequence identifier, e.g., `OP0001-24`.

3. **View Sequence**:

   - The sequence is visible in the Kanban and List views for CRM opportunities, providing an easy way to track leads.

Configuration
=============

- **No additional configuration is required** for this module. The sequence is automatically created and assigned to new opportunities.

Testing
=======

Test the following scenarios:

- **Opportunity Creation**:

  - Create a new CRM opportunity and verify that a unique sequence is automatically assigned.

- **View in Kanban and List**:

  - Verify that the sequence field appears in both the Kanban and List views of CRM opportunities.

Bug Tracker
===========

If you encounter any issues, please report them on the GitHub repository at `GitHub Issues <https://github.com/avanzosc/l10n-addons/issues>`_.

Credits
=======

Contributors
------------

* Unai Beristain <unaiberistain@avanzosc.es>
* Ana Juaristi <anajuaristi@avanzosc.es>

For module-specific questions, please contact the contributors directly. Support requests should be made through the official channels.

License
=======

This project is licensed under the LGPL-3 License. For more details, please refer to the LICENSE file or visit <https://opensource.org/licenses/LGPL-3.0>.
