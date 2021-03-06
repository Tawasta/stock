.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================================================
Default stock location for product quantity updates
===================================================

* Configurable default location suggestion for the wizard
* Replaces the hardcoded default in Odoo core

Configuration
=============
* Set the default location in warehouse settings

Usage
=====
* Open a product form and click the "Update Qty On Hand" button as usual. The
  configured stock location is suggested as the default.

Known issues / Roadmap
======================
* User should not be in "Manage Lots / Serial Numbers" and "Manage Multiple
  Stock Locations" groups to view "Update Qty on Hand"-window. But viewing
  this window preserved when user was added to these groups.

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@tawasta.fi>
* Timo Kekäläinen <timo.kekalainen@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
