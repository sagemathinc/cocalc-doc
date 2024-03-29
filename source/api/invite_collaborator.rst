invite_collaborator
===================

-  ``id``: A unique UUID for the query
-  ``project_id``: project_id of project into which user is invited
   (required)
-  ``account_id``: account_id of invited user (required)
-  ``title``: Title of the project
-  ``link2proj``: The full URL link to the project
-  ``replyto``: Email address of user who is inviting someone
-  ``replyto_name``: Name of user who is inviting someone
-  ``email``: Body of email user is sending (plain text or HTML)
-  ``subject``: Subject line of invitation email

Invite a user who already has a CoCalc account to become a collaborator
on a project. You must be owner or collaborator on the target project.
The user will receive an email notification.

Example:

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d account_id=99ebde5c-58f8-4e29-b6e4-b55b8fd71a1b \
       -d project_id=18955da4-4bfa-4afa-910c-7f2358c05eb8 \
       https://cocalc.com/api/v1/invite_collaborator
     ==> {"event":"success",
          "id":"e80fd64d-fd7e-4cbc-981c-c0e8c843deec"}

