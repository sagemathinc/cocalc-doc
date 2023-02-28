email-address-from-account-id
=============================

Using the CoCalc API to get the email address of a user from their account_id
*****************************************************************************

We assume you can do a basic query as explained in
:doc:`purchasing-licenses`.

If your API key is for an account with elevated privileges, i.e., an
``admin`` or ``partner``, then you can get the email address associated
with any account_id, as illustrated below.

NOTE: Some accounts in CoCalc do not have any email address associated
to them, in which case this api call will return an email address of
``undefined``. For example anonymous accounts have no identifying
information at all. As another example, if a user creates an account
using single-sign on via GitHub or Twitter, then they also may not have
an email address, since GitHub and Twitter don’t provide email.

Email address of a user
-----------------------

Put the account_id below of the user whose email address you want to
look up:

.. code:: sh

   curl -sk -u $key: -H 'Content-Type: application/json' \
      -d '{"account_id":"a407dd35-c960-481c-123F-1238c868ff8b"}' \
      $url/accounts/get-email-address

Result:

.. code:: js

   {"email_address":"joe@example.com"}
