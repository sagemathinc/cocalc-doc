unlink_passport
===============

-  ``strategy``: passport strategy (required)
-  ``id``: numeric id for user and passport strategy (required)

Unlink a passport auth for the account.

Strategies are defined in the database and may be viewed at
`/auth/strategies <https://cocalc.com/auth/strategies>`__.

Example:

Get passport id for some strategy for current user.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -H "Content-Type: application/json" \
       -d '{"query":{"accounts":{"account_id":"e6993694-820d-4f78-bcc9-10a8e336a88d","passports":null}}}' \
       https://cocalc.com/api/v1/query
     ==> {"query":{"accounts":{"account_id":"e6993694-820d-4f78-bcc9-10a8e336a88d",
                               "passports":{"facebook-14159265358":{"id":"14159265358",...}}}},
          "multi_response":false,
          "event":"query",
          "id":"a2554ec8-665b-495b-b0e2-8e248b54eb94"}

Unlink passport for that strategy and id.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d strategy=facebook \
       -d id=14159265358 \
       https://cocalc.com/api/v1/unlink_passport
     ==> {"event":"success",
          "id":"14159265358"}

Note that success is returned regardless of whether or not passport was
linked for the given strategy and id before issuing the API command.

