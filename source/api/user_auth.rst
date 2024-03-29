user_auth
=========

-  ``id``: A unique UUID for the query
-  ``account_id``: account_id for account to get an auth token for
   (required)
-  ``password``: password for account to get token for (required)

.. index:: pair: Token; Authentication Example:

Obtain a temporary authentication token for an account, which is a 24
character string. Tokens last for **12 hours**. You can only obtain an
auth token for accounts that have a password.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d account_id=99ebde5c-58f8-4e29-b6e4-b55b8fd71a1b \
       -d password=secret_password \
       https://cocalc.com/api/v1/user_auth
     ==> {"event":"user_auth_token","id":"9e8b68ac-08e8-432a-a853-398042fae8c9","auth_token":"BQokikJOvBiI2HlWgH4olfQ2"}

You can now use the auth token to craft a URL like this:

::

   https://cocalc.com/app?auth_token=BQokikJOvBiI2HlWgH4olfQ2

and provide that to a user. When they visit that URL, they will be
temporarily signed in as that user.

