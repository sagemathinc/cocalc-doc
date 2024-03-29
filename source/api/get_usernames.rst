get_usernames
=============

-  ``id``: A unique UUID for the query
-  ``account_ids``: list of account_ids (required)

Get first and last names for a list of account ids.

Note: Options for the ``get_usernames`` API message must be sent as JSON
object.

Example:

::

     curl -u sk_abcdefQWERTY090900000000: -H "Content-Type: application/json" \
       -d '{"account_ids":["cc3cb7f1-14f6-4a18-a803-5034af8c0004","9b896055-920a-413c-9172-dfb4007a8e7f"]}' \
       https://cocalc.com/api/v1/get_usernames
     ==>  {"event":"usernames",
           "id":"32b485a8-f214-4fda-a622-4dbfe0db2b9c",
           "usernames": {
              "cc3cb7f1-14f6-4a18-a803-5034af8c0004":{"first_name":"John","last_name":"Smith"},
              "9b896055-920a-413c-9172-dfb4007a8e7f":{"first_name":"Jane","last_name":"Doe"}}}

