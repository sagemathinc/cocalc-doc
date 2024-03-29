public_get_text_file
====================

-  ``id``: A unique UUID for the query
-  ``project_id``: id of project containing public file to be read
   (required)
-  ``path``: path to file to be read in target project (required)

Read a public (shared) text file in the project whose id is supplied.
User does not need to be owner or collaborator in the target project and
does not need to be logged into CoCalc. Argument ``path`` is relative to
home directory in target project.

Security key may be blank.

Examples

Read a public file.

::

     curl -u : \
       -d project_id=e49e86aa-192f-410b-8269-4b89fd934fba \
       -d path=Public/hello.txt
       https://cocalc.com/api/v1/public_get_text_file
     ==> {"event":"public_text_file_contents",
          "id":"2d0e2faa-893a-44c1-9f64-59203bbbb017",
          "data":"hello world\nToday is Friday\n"}

Attempt to read a file which is not public.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d project_id=e49e86aa-192f-410b-8269-4b89fd934fba \
       -d path=Private/hello.txt
       https://cocalc.com/api/v1/public_get_text_file
     ==> {"event":"error","id":"0288b7d0-dda9-4895-87ba-aa71929b2bfb",
          "error":"path 'Private/hello.txt' of project with id 'e49e86aa-192f-410b-8269-4b89fd934fba' is not public"}

