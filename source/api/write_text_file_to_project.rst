write_text_file_to_project
==========================

-  ``id``: A unique UUID for the query
-  ``project_id``: id of project where file is created (required)
-  ``path``: path to file, relative to home directory in destination
   project (required)
-  ``content``: contents of the text file to be written (required)

Create a text file in the target project with the given ``project_id``.
Directories containing the file are created if they do not exist
already. If a file already exists at the destination path, it is
overwritten.

**Note:** You need to have read access to the project. The Linux user
``user`` in the target project must have permissions to create files and
containing directories if they do not already exist.

Example:

Create a text file.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d project_id=e49e86aa-192f-410b-8269-4b89fd934fba \
       -d "content=hello$'\n'world" \
       -d path=Assignments/A1/h1.txt \
       https://cocalc.com/api/v1/write_text_file_to_project

