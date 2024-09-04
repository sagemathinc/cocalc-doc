.. index:: Vouchers

======================
Vouchers
======================

.. contents::
   :local:
   :depth: 2


.. figure:: img/voucher_center.png
    :width: 90%
    :align: center
    :alt: voucher center

    ..
    
.. _credit-vouchers:

################################
CoCalc Credit Vouchers
################################

CoCalc credit voucher codes are single-use codes that you can purchase and make available to somebody else, who can then redeem them at https://cocalc.com/redeem for that amount of credit on their CoCalc account. They can then buy anything in CoCalc using that credit, including upgrade licenses, dedicated VM's and disks, pay-as-you-go project upgrades, student-pay course upgrades, GPT-4 chat evaluation, more vouchers, etc.

See `ANN: Cash Vouchers <https://github.com/sagemathinc/cocalc/discussions/6857>`_ for the feature announcement and discussion.

################################
CoCalc License Vouchers
################################

CoCalc license voucher codes are single-use codes that can be redeemed for licenses. Distributing these codes is similar to distributing licenses, except that the keys do not circulate during distribution. In fact, license keys are not created until codes are redeemed by end users.

See `ANN: Vouchers - transferable codes that can be renewed later for a license <https://github.com/sagemathinc/cocalc/discussions/6534>`_ for the feature announcement and discussion.

################################
Examples of Voucher Use
################################

***************************
Hosting a Workshop
***************************

Vouchers can be useful for running a workshop on CoCalc, offering simpler setup than CoCalc managed courses when attendees are not known until just before a session starts. Vouchers can be redeemed without going through the exchange of email addresses needed for a managed course.

***************************
CoCalc Administrators
***************************

An administrator of :ref:`cocalc_onprem` may wish to create and issue vouchers to potential users of their CoCalc installation.

*******************************
CoCalc Resellers and Bookstores
*******************************

You can resell vouchers for a particular preconfigured type of license or for a given amount of CoCalc credit. In the second case you first have to figure out how much the required purchase will cost the students (e.g., at `https://cocalc.com/store/site-license <https://cocalc.com/store/site-license?user=academic&period=range&run_limit=1&member=true&uptime=short&cpu=1&ram=2&disk=3&range=2023-10-30T03%3A46%3A21.414Z_2024-03-01T04%3A46%3A21.414Z>`_ or from within the course configuration). The way CoCalc works now is that every account has a credit balance, and all purchases use this balance. Vouchers make it easy to enter a code at https://cocalc.com/redeem which then adds credit to a student's account, which they can then use to purchase anything in CoCalc, e.g., to pay for the license for a course, project upgrades, GPU pay as you go soon, etc.

Once the required amount is determined, you can buy a list of CoCalc credit voucher codes from https://cocalc.com/store/vouchers for this amount. You will get a downloadable spreadsheet listing all of the codes. You can also check online at any time at https://cocalc.com/vouchers to see the exact status of all codes (have they been redeemed?, etc.). You can then sell the voucher codes to the students.

*********************************
No Special Arrangement Is Needed
*********************************

You can purchase and resell vouchers without any special arrangement with us. It is perfectly OK to mark up the price of the vouchers if you feel you need to cover the labor involved.

################################
Obtaining a Voucher
################################

********************************
Obtaining a Credit Voucher
********************************

.. raw:: html

    <center><iframe
        width="640" height="360"
        src="https://www.youtube.com/embed/4eyngZPNHQY?si=s1_kAwqKnVo0PShb"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
    </iframe></center>
    
If your shopping card it empty, then to buy a CoCalc credit voucher simply go to https://cocalc.com/store/vouchers, enter the desired amount, and click "Add to Cart":

.. figure:: img/obtain_credit_voucher.png
    :width: 90%
    :align: center
    :alt: Entering amount for a credit voucher.

    Entering amount for a credit voucher.

If you already have some other items in your cart, you can add a CoCalc credit voucher in addition to them by selecting "Add Cash Voucher":

.. figure:: img/add_credit_voucher.png
    :width: 90%
    :align: center
    :alt: Adding a credit voucher to other items.

    Adding a credit voucher to other items.

********************************
Obtaining a License Voucher
********************************

You must have at least one **non-subscription** item in `your shopping cart <https://cocalc.com/store/cart.>`_ to create license vouchers. Shop for upgrades, a license boost, or a dedicated VM or disk, and select a specific range of dates. Then go to https://cocalc.com/store/vouchers or click "Create Vouchers" from the shopping cart:

.. figure:: img/create_voucher_from_cart.png
    :width: 90%
    :align: center
    :alt: Shopping cart with 1 item before creating a voucher.

    Shopping cart with 1 item before creating a voucher.

********************************
Configuring the Voucher
********************************

Configure the voucher by entering the number of codes that you need, its description, etc.

.. figure:: img/configure_voucher.png
    :width: 90%
    :align: center
    :alt: Configure the voucher.

    Configure the voucher.

********************************
Creating the Voucher
********************************

After configuring the voucher, click "Create *n* Vouchers" to pay, if necessary, and create your voucher with *n* codes. You will see a confirmation screen.

.. figure:: img/voucher-order-complete.png
    :width: 90%
    :align: center
    :alt: Voucher order confirmation.

    Voucher order confirmation.

In the upper part of the screen, you will see one or more links, with the caption, "You can download the corresponding voucher codes via the links below". The topmost link will take you to the codes for the new voucher.

********************************
Downloading Voucher Codes
********************************

You can download the voucher codes immediately by clicking the link under "Order Complete!" above. You can also `view and download codes <https://cocalc.com/vouchers/created>`_ for any vouchers at any time.

.. figure:: img/view-codes.png
    :width: 90%
    :align: center
    :alt: Display codes for a specific voucher.

    Display codes for a specific voucher.

********************************
Distributing Codes to Users
********************************

Once you have the voucher codes, you can distribute them by any means of your choice, for example email or text message. When you look at the list of codes there is a "Private Notes" field where you can keep track of what you have done with each voucher.

Here is some sample text you might use when sending out voucher codes::

   You can redeem this code at https://cocalc.com/redeem

   If you want to easily apply the license provided by this
   voucher to a project, open that project's settings and
   click the "Redeem Voucher" button. (You can do this with
   the same voucher multiple times for different projects.)

********************************
Redeeming Voucher Codes
********************************

To redeem a voucher, visit the `code redemption page <https://cocalc.com/redeem>`_ and enter the voucher code:

.. figure:: img/enter-voucher-code.png
    :width: 70%
    :align: center
    :alt: entering a code

    entering the voucher code

With a license voucher you can also obtain a license key by selecting a project and scrolling down to "Redeem a voucher" in :doc:`project-settings`:

.. figure:: img/redeem-a-code.png
    :width: 80%
    :align: center
    :alt: redeeming a code

    redeem voucher code button in project settings

When a user redeems a code, the corresponding license(s) start at the time of redemption and last for the same number of days as the original shopping cart item(s) used to create the voucher.

An end user can view all the voucher codes they have redeemed by browsing to the `redeemed voucher page <https://cocalc.com/vouchers/redeemed>`_.

.. figure:: img/vouchers-you-redeemed.png
    :width: 90%
    :align: center
    :alt: vouchers you redeemed

    ..

################################
Status of Vouchers Created
################################

For any voucher you have created, you can download all codes and view the status of all codes for any voucher at the `created vouchers page <https://cocalc.com/vouchers/created>`_.

.. figure:: img/your-vouchers.png
    :width: 90%
    :align: center
    :alt: display of created vouchers

    status of created vouchers


############################
Questions?
############################

If you want to try out using a voucher (or have any other questions), let us know. You can open a support request while signed into CoCalc by clicking :ref:`help-button` at upper right, or just send an email to help@cocalc.com.

