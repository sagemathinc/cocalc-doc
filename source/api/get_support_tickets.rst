get_support_tickets
===================

-  ``id``: A unique UUID for the query

Fetch information on support tickets for the user making the request.
See the example for details on what is returned.

Notes:

-  There may be a delay of several minutes between the time a support
   ticket is created with a given ``account_id`` and the time that
   ticket is available to the account owner via ``get_support_tickets``.
-  Field ``account_id`` is not required because it is implicit from the
   request.
-  Archived tickets are not returned.

Example:

::

   curl -u sk_abcdefQWERTY090900000000:  -X POST \
       https://cocalc.com/api/v1/get_support_tickets
     ==> {"event":"support_tickets",
          "id":"58bfd6f4-fd63-4602-82b8-676d92f8b0b8",
          "tickets":[{"id":1234,
                      "subject":"package xyz",
                      "description":"package xyz\n\nhttps://cocalc.com/projects/0010abe1-9283-4b42-b403-fa4fc1e3be57/worksheet.sagews\n\nCourse: https://cocalc.com/projects/cc8f1243-d573-4562-9aab-c15a3872d683",
                      "created_at":"2017-07-05T14:28:38Z",
                      "updated_at":"2017-07-05T14:29:29Z",
                      "status":"open",
                      "url":"https://sagemathcloud.zendesk.com/requests/0123"}]}

