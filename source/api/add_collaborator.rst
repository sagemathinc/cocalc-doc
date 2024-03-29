add_collaborator
================

-  ``id``: A unique UUID for the query
-  ``project_id``: project_id of project to add user to (can be an array
   to add multiple users to multiple projects); isn’t needed if token_id
   is specified
-  ``account_id``: account_id of user (can be an array to add multiple
   users to multiple projects) (required)
-  ``token_id``: project_invite_token that is needed in case the user
   **making the request** is not already a project collab

Directly add a user to a CoCalc project. You must be owner or
collaborator on the target project or provide, an optional valid
token_id (the token determines the project). The user is NOT notified
via email that they were added, and there is no confirmation process.
(Eventually, there will be an accept process, or this endpoint will only
work with a notion of “managed accounts”.)

You can optionally add multiple user to multiple projects by padding an
array of strings for project_id and account_id. The arrays must have the
same length.

Example:

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d account_id=99ebde5c-58f8-4e29-b6e4-b55b8fd71a1b \
       -d project_id=18955da4-4bfa-4afa-910c-7f2358c05eb8 \
       https://cocalc.com/api/v1/add_collaborator
     ==> {"event":"success",
          "id":"e80fd64d-fd7e-4cbc-981c-c0e8c843deec"}
