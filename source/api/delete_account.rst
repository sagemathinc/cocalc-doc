delete_account
==============

-  ``id``: A unique UUID for the query
-  ``account_id``: account_id for account to be deleted (required)

Example:

Delete an existing account:

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d account_id=99ebde5c-58f8-4e29-b6e4-b55b8fd71a1b \
       https://cocalc.com/api/v1/delete_account
     ==> {"event":"account_deleted","id":"9e8b68ac-08e8-432a-a853-398042fae8c9"}

Event ``account_deleted`` is also returned if the account was already
deleted before the API call, or if the account never existed.

After successful ``delete_account``, the owner of the deleted account
will not be able to login, but will still be listed as collaborator or
owner on projects which the user collaborated on or owned respectively.

