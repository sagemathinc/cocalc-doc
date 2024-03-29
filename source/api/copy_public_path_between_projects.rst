copy_public_path_between_projects
=================================

-  ``id``: A unique UUID for the query
-  ``src_project_id``: id of source project (required)
-  ``src_path``: relative path of directory or file in the source
   project (required)
-  ``target_project_id``: id of target project (required)
-  ``target_path``: defaults to src_path
-  ``overwrite_newer``: overwrite newer versions of file at destination
   (destructive) (default: false)
-  ``delete_missing``: delete files in dest that are missing from source
   (destructive) (default: false)
-  ``backup``: make ~ backup files instead of overwriting changed files
   (default: false)
-  ``timeout``: how long to wait for the copy to complete before
   reporting error (though it could still succeed)
-  ``exclude_history``: if true, exclude all files of the form
   ``*.sage-history`` (default: false)

Copy a file or directory from a public project to a target project.

**Note:** the ``timeout`` option is passed to a call to the ``rsync``
command. If no data is transferred for the specified number of seconds,
then the copy terminates. The default is 0, which means no timeout.

**Note:** You need to have write access to the target project.

Example:

Copy public file ``PUBLIC/doc.txt`` from source project to private file
``A/sample.txt`` in target project.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d src_project_id=e49e86aa-192f-410b-8269-4b89fd934fba \
       -d src_path=PUBLIC/doc.txt \
       -d target_project_id=2aae4347-214d-4fd1-809c-b327150442d8 \
       -d target_path=A/sample.txt \
       https://cocalc.com/api/v1/copy_public_path_between_projects
     ==> {"event":"success",
          "id":"45d851ac-5ea0-4aea-9997-99a06c054a60"}

