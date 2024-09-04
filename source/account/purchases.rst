.. index:: Account Purchases
.. _account-purchases:

==================================
Purchases
==================================

.. contents::
   :local:
   :depth: 1


To view the Purchases panel, first open the :ref:`project-list`, then click **Account** at upper right, then **Purchases**. You can also view the **Purchases** panel by browsing to https://cocalc.com/settings/purchases

.. note::

    CoCalc's purchasing system has been upgraded as of August, 2023. Here's the CoCalc feature announcement and discussion: `ANN: CoCalc's New Purchasing System <https://github.com/sagemathinc/cocalc/discussions/6848>`_.


Account Balance
================

.. figure:: img/purch01.png
     :width: 90%
     :align: center
     :alt: Account Balance on Purchases Panel

     Account Balance on Purchases Panel

Account balance information is displayed in the upper part of the **Purchases** panel.


.. _automatic-payments:

Enable/Disable Automatic Payments
==================================

Once on the **Purchases** panel, click the **Enable Automatic Payments** button to open the pop-up window that allows you to initiate a Stripe checkout session to enter your payment information:

.. figure:: img/enable-auto-pay.png
     :width: 90%
     :align: center
     :alt: Enable Automatic Payments Pop-up

     Enable Automatic Payments Pop-up

If you already had automatic payments enabled, you will have an option to disable them instead.


Transactions, Limits, and Plots
================================

.. figure:: img/purch02.png
     :width: 90%
     :align: center
     :alt: Transactions on the Purchases Panel

     Transactions on the Purchases Panel
     
Several views of transactions for your account are available in the lower part of the **Purchases** panel.


.. index:: Account Tab; subscription list
.. _account-subscriptions:
.. _subscription-list:
.. _subscriptions-update:

Subscriptions
=============

To buy a license subscription, visit https://cocalc.com/store/site-license

You can optionally :ref:`automatic-payments`

To view your currently active subscriptions, go to https://cocalc.com/settings/subscriptions

.. figure:: img/new-subscr.png
     :width: 90%
     :align: center
     :alt: Subscriptions
     
     Subscriptions
     
       
- A few days before your subscription renews, you will get an email reminder

- It is possible to have a subscription without having any automatic payment method on file. Instead, when the renewal date is near, you get an email that you should add credit to your account to cover the subscription renewal. This is valuable to people in some countries, like India, where automatic subscription renewals are heavily regulated by law.

- You can edit your subscription (e.g., increase the RAM quota it provides) at any time, and you only pay the prorated difference.

- If you cancel your subscription, you can resume it later, rather than having to create a new subscription. Subscriptions are resumed at the current rates.


Subscriptions (legacy page)
===========================

You can still use your active legacy subscriptions by clicking "Legacy Subscriptions Page..." at the bottom of the **Subscriptions** panel.

The legacy subscriptions section lists your currently active license subscriptions, personal plans, and course packages.
The word "Active" denotes ordinary active subscriptions.
The word "Trialing" indicates a free trial or other custom subscription plan.

.. note::

    If you have further questions about course packages, subscriptions, or upgrades,
    please consult the :ref:`upgrades-faq`!


Invoices and receipts
=========================

The "Invoices and receipts" section shows a list of CoCalc purchases made using the order process on this page.

.. figure:: img/account/three-rcpt-hidden.png
     :width: 90%
     :align: center
     :alt: condensed list of receipts

     view of receipts

.. figure:: img/account/three-rcpt-shown.png
     :width: 90%
     :align: center
     :alt: expanded list of receipts

     view of receipts showing details for each item

API v2 endpoint
=================

If you're interested in automating access to purchase data, see the `API v2 endpoint to get purchases <https://doc.cocalc.com/api2/get-purchases.html>`_.
