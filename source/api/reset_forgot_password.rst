reset_forgot_password
=====================

-  ``id``: A unique UUID for the query
-  ``reset_code``: id code that was sent in a password reset email
   (required)
-  ``new_password``: must be between 6 and 64 characters in length
   (required)

Reset password, given reset code.

Example:

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d reset_code=35a0eea6-370a-45c3-ab2f-3210df68748f \
       -d new_password=qjqhddfsfj \
       https://cocalc.com/api/v1/reset_forgot_password
     ==> {"event":"reset_forgot_password_response","id":"85bd6027-644d-4859-9e17-5e835bd47570","error":false}

