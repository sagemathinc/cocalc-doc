remove_collaborator
===================

-  ``id``: A unique UUID for the query
-  ``project_id``: project_id of project from which user is removed
   (required)
-  ``account_id``: account_id of removed user (required)

Remove a user from a CoCalc project. You must be owner or collaborator
on the target project. The project owner cannot be removed. The user is
NOT notified via email that they were removed.

Example:

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d account_id=99ebde5c-58f8-4e29-b6e4-b55b8fd71a1b \
       -d project_id=18955da4-4bfa-4afa-910c-7f2358c05eb8 \
       https://cocalc.com/api/v1/remove_collaborator
     ==> {"event":"success",
          "id":"e80fd64d-fd7e-4cbc-981c-c0e8c843deec"}

