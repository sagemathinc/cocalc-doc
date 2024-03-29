create_support_ticket
=====================

-  ``id``: A unique UUID for the query
-  ``username``: name on the ticket
-  ``email_address``: if there is no email_address in the account, there
   cannot be a ticket! (required)
-  ``subject``: like an email subject (required)
-  ``body``: html or md formatted text (required)
-  ``tags``: a list of tags, like ``['member']``
-  ``account_id``: account_id for the ticket
-  ``location``: from the URL, to know what the requester is talking
   about
-  ``info``: additional data dict, like browser/OS

Open a CoCalc support ticket.

Notes:

-  If ``account_id`` is not provided, the ticket will be created, but
   ticket info will not be returned by ``get_support_tickets``.

-  If ``username`` is not provided, ``email_address`` is used for the
   name on the ticket.

-  ``location`` is used to provide a path to a specific project or file,
   for example

   ::

      /project/a17037cb-a083-4519-b3c1-38512af603a6/files/notebook.ipynb`

If present, the ``location`` string will be expanded to a complete URL
and appended to the body of the ticket.

-  The ``info`` dict can be used to provide additional metadata, for
   example

   ::

      {"user_agent":"Mozilla/5.0 ... Chrome/58.0.3029.96 Safari/537.36"}

-  If the ticket concerns a CoCalc course, the project id of the course
   can be included in the ``info`` dict, for example,

   ::

      {"course":"0c7ae00c-ea43-4981-b454-90d4a8b1ac47"}

   In that case, the course project_id will be expanded to a URL and
   appended to the body of the ticket.

-  If ``tags`` or ``info`` are provided, options must be sent as a JSON
   object.

Example:

::

     curl -u sk_abcdefQWERTY090900000000: -H "Content-Type: application/json" \
       -d '{"email_address":"jd@example.com", \
            "subject":"package xyz", \
            "account_id":"291f43c1-deae-431c-b763-712307fa6859", \
            "body":"please install package xyz for use with Python3", \
            "tags":["member"], \
            "location":"/projects/0010abe1-9283-4b42-b403-fa4fc1e3be57/worksheet.sagews", \
            "info":{"user_agent":"Mozilla/5.0","course":"cc8f1243-d573-4562-9aab-c15a3872d683"}}' \
       https://cocalc.com/api/v1/create_support_ticket
     ==> {"event":"support_ticket_url",
          "id":"abd649bf-ea2d-4952-b925-e44c6903945e",
          "url":"https://sagemathcloud.zendesk.com/requests/0123"}

