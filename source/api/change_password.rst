change_password
===============

-  ``id``: A unique UUID for the query
-  ``account_id``: account id of the account whose password is being
   changed (required)
-  ``old_password``: (default: ““)
-  ``new_password``: must be between 6 and 64 characters in length
   (required)

Given account_id and old password for an account, set a new password.

Example:

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d account_id=... \
       -d old_password=... \
       -d new_password=... \
       https://cocalc.com/api/v1/change_password
     ==> {"event":"changed_password","id":"41ff89c3-348e-4361-ad1d-372b55e1544a"}

