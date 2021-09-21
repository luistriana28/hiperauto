==============
Price Security
==============

Creates a new permission to restrict the users that can modify the prices
of the products.

Asociate to each user a list of pricelist and the correspoding discounts they
can apply to sale orders and invoices.

Allow the posibility to mark products so that anyone can modify their price in
a sale order.

Add a sequence field on pricelist and payment term (you can only assign pricelist or terms of lower priority than partner default one)

Installation
============

To install this module, you need to:

#. Just install this module.

Configuration
=============

To configure this module, you need to:

#. Set 'Restrict Prices' for users you want to restrict.
#. For the same users, configure discounts range on "Discounts Permissions" users tab.

Usage
=====

To use this module, you need to:

For users with price restriction, it restricts:
#. on sales orders: change payment term or pricelist
#. on sales order lines: change unit price and set limits on discount (limits configured on user)
#. on partners: change payment term or pricelist
#. on invoices: change unit price
#. on invoice lines: change unit price and set limits on discount (limits configured on user)
#. on product: change price

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/ingadhoc/product/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

ADHOC SA

Contributors
------------

Maintainer
----------

This module is maintained by the Luis Triana.

To contribute to this module, please visit https://www.github.com/luistriana28/hiperauto.
