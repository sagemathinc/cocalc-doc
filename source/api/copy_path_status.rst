copy_path_status
================

-  ``copy_path_id``: A unique UUID for a copy path operation
-  ``src_project_id``: Source of copy operation to filter on
-  ``target_project_id``: Target of copy operation to filter on
-  ``src_path``: (src/targ only) Source path of copy operation to filter
   on
-  ``limit``: (src/targ only) maximum number of results (max 1000)
   (default: 1000)
-  ``offset``: (src/targ only) default 0; set this to a multiple of the
   limit
-  ``pending``: (src/targ only) true returns copy ops, which did not
   finish yet (default: true) (default: true)
-  ``failed``: (src/targ only) if true, only show finished and failed
   copy ops (default: false) (default: false)

Retrieve status information about copy path operation(s).

There are two ways to query:

-  **single result** for a specific ``copy_path_id``, which was returned
   by ``copy_path_between_projects`` earlier;
-  **array of results**, for at last one of ``src_project_id`` or
   ``target_project_id``, and additionally filtered by an optionally
   given ``src_path``.

Check for the field ``"finished"``, containing the timestamp when the
operation completed. There might also be an ``"error"``!

**Note:** You need to have read/write access to the associated
src/target project.

