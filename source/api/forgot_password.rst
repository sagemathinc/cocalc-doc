forgot_password
===============

-  ``id``: A unique UUID for the query
-  ``email_address``: email address for account requesting password
   reset (required)

Given the email address of an existing account, send password reset
email.

Example:

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d email_address=... \
       https://cocalc.com/api/v1/forgot_password
     ==> {"event":"forgot_password_response",
          "id":"26ed294b-922b-47e1-8f3f-1e54d8c8e558",
          "error":false}

