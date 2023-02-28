ping
====

-  ``id``: A unique UUID for the query

Test API connection, return time as ISO string when server responds to
ping. Security key is required. Request id is optional.

Examples:

Omitting request id:

::

     curl -X POST -u sk_abcdefQWERTY090900000000: https://cocalc.com/api/v1/ping
     ==> {"event":"pong","id":"c74afb40-d89b-430f-836a-1d889484c794","now":"2017-05-24T13:29:11.742Z"}

Using ``uuid`` shell command to create a request id:

::

     uuid
     ==> 553f2815-1508-416d-8e69-2dde5af3aed8
     curl -u sk_abcdefQWERTY090900000000: https://cocalc.com/api/v1/ping -d id=553f2815-1508-416d-8e69-2dde5af3aed8
     ==> {"event":"pong","id":"553f2815-1508-416d-8e69-2dde5af3aed8","now":"2017-05-24T13:47:21.312Z"}

Using JSON format to provide request id:

::

     curl -u sk_abcdefQWERTY090900000000: -H "Content-Type: application/json" \
       -d '{"id":"8ec4ac73-2595-42d2-ad47-0b9641043b46"}' https://cocalc.com/api/v1/ping
     ==> {"event":"pong","id":"8ec4ac73-2595-42d2-ad47-0b9641043b46","now":"2017-05-24T17:15:59.288Z"}

