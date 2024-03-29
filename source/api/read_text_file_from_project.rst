read_text_file_from_project
===========================

-  ``id``: A unique UUID for the query
-  ``project_id``: id of project containing file to be read (or array of
   project_id’s) (required)
-  ``path``: path to file to be read in target project (or array of
   paths) (required)

Read a text file in the project whose ``project_id`` is supplied.

Argument ``'path'`` is relative to home directory in target project.

You can also read multiple ``project_id``/``path``\ ’s at once by making
``project_id`` and ``path`` arrays (of the same length). In that case,
the result will be an array of ``{project_id, path, content}`` objects,
in some random order. If there is an error reading a particular file,
instead ``{project_id, path, error}`` is included.

**Note:** You need to have read access to the project, the Linux user
``user`` in the target project must have permissions to read the file
and containing directories.

Example:

Read a text file.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d project_id=e49e86aa-192f-410b-8269-4b89fd934fba \
       -d path=Assignments/A1/h1.txt \
       https://cocalc.com/api/v1/read_text_file_from_project
     ==> {"event":"text_file_read_from_project",
          "id":"481d6055-5609-450f-a229-480e518b2f84",
          "content":"hello"}

