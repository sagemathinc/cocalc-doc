invite_noncloud_collaborators
=============================

-  ``id``: A unique UUID for the query
-  ``project_id``: project_id of project into which users are invited
   (required)
-  ``to``: comma- or semicolon-delimited string of email addresses
   (required)
-  ``email``: body of the email to be sent, may include HTML markup
   (required)
-  ``title``: string that will be used for project title in the email
   (required)
-  ``link2proj``: URL for the target project (required)
-  ``replyto``: Reply-To email address
-  ``replyto_name``: Reply-To name
-  ``subject``: email Subject

Invite users who do not already have a CoCalc account to join a project.
An invitation email is sent to each user in the ``to`` option.
Invitation is not sent if there is already a CoCalc account with the
given email address. You must be owner or collaborator on the target
project.

Limitations: - Total length of the request message must be less than or
equal to 1024 characters. - Length of each email address must be less
than 128 characters.

Example:

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d project_id=18955da4-4bfa-4afa-910c-7f2358c05eb8 \
       -d to=someone@m.local \
       -d 'email=Please sign up and join this project.' \
       -d 'title=Class Project' \
       -d link2proj=https://cocalc.com/projects/18955da4-4bfa-4afa-910c-7f2358c05eb8 \
       https://cocalc.com/api/v1/invite_noncloud_collaborators
     ==>  {"event":"invite_noncloud_collaborators_resp",
           "id":"39d7203d-89b1-4145-8a7a-59e41d5682a3",
           "mesg":"Invited someone@m.local to collaborate on a project."}

Email sent by the previous example:

::

   To: someone@m.local
   From: CoCalc <invites@cocalc.com
   Reply-To: help@cocalc.com
   Subject: CoCalc Invitation

   Please sign up and join this project.<br/><br/>\n<b>
   To accept the invitation, please sign up at\n
   <a href='https://cocalc.com'>https://cocalc.com</a>\n
   using exactly the email address 'someone@m.local'.\n
   Then go to <a href='https://cocalc.com/projects/18955da4-4bfa-4afa-910c-7f2358c05eb8'>
   the project 'Team Project'</a>.</b><br/>

