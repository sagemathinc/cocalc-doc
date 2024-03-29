create_account
==============

-  ``id``: A unique UUID for the query
-  ``password``: if given, must be between 6 and 64 characters in length
-  ``agreed_to_terms``: must be true or user will get nagged
-  ``token``: account creation token - see src/dev/docker/README.md
-  ``get_api_key``: if set to anything truth-ish, will create (if
   needed) and return api key with signed_in message
-  ``usage_intent``: response to Cocalc usage intent at sign up

Examples:

Create a new account:

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d first_name=John00 \
       -d last_name=Doe00 \
       -d email_address=jd@example.com \
       -d password=xyzabc09090 \
       -d agreed_to_terms=true https://cocalc.com/api/v1/create_account

Option ``agreed_to_terms`` must be present and specified as true.
Account creation fails if there is already an account using the given
email address, if ``email_address`` is improperly formatted, and if
password is fewer than 6 or more than 64 characters.

Attempting to create the same account a second time results in an error:

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d first_name=John00 \
       -d last_name=Doe00 \
       -d email_address=jd@example.com \
       -d password=xyzabc09090 \
       -d agreed_to_terms=true https://cocalc.com/api/v1/create_account
     ==> {"event":"account_creation_failed",
          "id":"2332be03-aa7d-49a6-933a-cd9824b7331a",
          "reason":{"email_address":"This e-mail address is already taken."}}

