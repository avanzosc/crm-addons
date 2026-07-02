.. image:: https://img.shields.io/badge/license-LGPL--3-blue.svg
   :target: https://opensource.org/licenses/LGPL-3.0
   :alt: License: LGPL-3

==========================================
CRM Lead Stage and Action Schedule Meeting
==========================================

Overview
========

The **CRM Lead Stage and Action Schedule Meeting** module enhances the CRM lead management in Odoo by introducing additional stages for leads and enabling automatic meeting scheduling from leads.

Features
========

- **Custom Lead Stages**:
  
  - Allows for different stages in the CRM leads based on the team associated with the lead.

- **Automatic Meeting Scheduling**:
  
  - Provides the capability to automatically schedule meetings from leads, ensuring timely follow-ups.

- **User Access**:
  
  - Grants read, write, create, and unlink permissions on the CRM lead model to users in the `base.group_user` group.

Usage
=====

Once the module is installed:

- **Lead Stages**:
  
  - You can now assign different stages to leads, which are filtered based on the associated team.

- **Meeting Scheduling**:
  
  - Use the "Schedule Meeting" button to automatically generate a meeting from a lead.

Configuration
=============

1. **Access Rights**:

   - Ensure that users have the necessary access rights to view and modify leads and schedule meetings.

2. **Lead Stages**:

   - Configure and customize lead stages as needed from the CRM settings.

Testing
=======

Test the following functionalities:

- **Lead Form View**:
  
  - Check that the new stages and meeting scheduling options are available and working correctly.

- **Permissions**:
  
  - Verify that users have the correct permissions as defined in `security/ir.model.access.csv`.

Bug Tracker
===========

For bugs and issues, please visit `GitHub Issues <https://github.com/avanzosc/project-addons/issues>`_ to report or track issues.

Credits
=======

Contributors
------------

* Unai Beristain <unaiberistain@avanzosc.es>
* Ana Juaristi <anajuaristi@avanzosc.es>

Please contact contributors for module-specific questions, but direct support requests should be made through the official channels.

License
=======
This project is licensed under the LGPL-3 License. For more details, please refer to the LICENSE file or visit <https://opensource.org/licenses/LGPL-3.0>.
