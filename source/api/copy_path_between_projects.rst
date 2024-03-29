copy_path_between_projects
==========================

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
-  ``timeout``: seconds to wait before reporting “error” (though copy
   could still succeed)
-  ``exclude_history``: if true, exclude all files of the form
   ``*.sage-history`` (default: false)
-  ``wait_until_done``: if false, the operation returns immediately with
   the copy_path_id for querying copy_path_status (default: true)
-  ``scheduled``: if set, the copy operation runs earliest after the
   given time and wait_until_done is false. Must be a ``new Date(...)``
   parseable string.

Copy a file or directory from one project to another.

**Note:** the ``timeout`` option is passed to a call to the ``rsync``
command. If no data is transferred for the specified number of seconds,
then the copy terminates. The default is 0, which means no timeout.

Relative paths (paths not beginning with ‘/’) are relative to the user’s
home directory in source and target projects.

**Note:** You need to have read/write access to the associated
src/target project.

Further options:

-  ``wait_until_done``: set this to false to immediately retrieve the
   ``copy_path_id``. This is the **recommended way** to use this
   endpoint, because a blocking request might time out and you’ll never
   learn about outcome of the copy operation. Learn about the status
   (success or failure, including an error message) via the
   :doc:``copy_path_status`` endpoint.
-  ``scheduled``: set this to a date in the future or postpone the copy
   operation. Suitable timestamps can be created as follows:

   -  Bash: 1 minute in the future
      ``date -d '+1 minute' --utc +'%Y-%m-%dT%H:%M:%S'``
   -  Python using `arrow <https://arrow.readthedocs.io/en/latest/>`__
      library:

      -  1 minute in the future:
         ``arrow.now('UTC').shift(minutes=+1).for_json()``
      -  At a specific time:
         ``arrow.get("2019-08-29 22:00").for_json()`` Later, learn about
         its outcome via :doc:``copy_path_status`` as well.

Example:

Copy file ``A/doc.txt`` from source project to target project. Folder
``A`` will be created in target project if it does not exist already.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d src_project_id=e49e86aa-192f-410b-8269-4b89fd934fba \
       -d src_path=A/doc.txt \
       -d target_project_id=2aae4347-214d-4fd1-809c-b327150442d8 \
       https://cocalc.com/api/v1/copy_path_between_projects
     ==> {"event":"success",
          "id":"45d851ac-5ea0-4aea-9997-99a06c054a60"}

