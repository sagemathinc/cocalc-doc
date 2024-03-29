change_email_address
====================

-  ``id``: A unique UUID for the query
-  ``account_id``: account_id for account whose email address is changed
   (required)
-  ``old_email_address``: ignored – deprecated (default: ““)
-  ``new_email_address``: (required)
-  ``password``: (default: ““)

Given the ``account_id`` for an account, set a new email address.

Examples:

Successful change of email address.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d account_id=99ebde5c-58f8-4e29-b6e4-b55b8fd71a1b \
       -d password=secret_password \
       -d new_email_address=new@email.com \
       https://cocalc.com/api/v1/change_email_address
     ==> {"event":"changed_email_address",
          "id":"8f68f6c4-9851-4b88-bd65-37cb983298e3",
          "error":false}

Fails if new email address is already in use.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d account_id=99ebde5c-58f8-4e29-b6e4-b55b8fd71a1b \
       -d password=secret_password \
       -d new_email_address=used@email.com \
       https://cocalc.com/api/v1/change_email_address
     ==> {"event":"changed_email_address",
          "id":"4501f022-a57c-4aaf-9cd8-af0eb05ebfce",
          "error":"email_already_taken"}

**Note:** ``account_id`` and ``password`` must match the ``id`` of the
current login.

