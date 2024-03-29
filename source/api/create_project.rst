create_project
==============

-  ``id``: A unique UUID for the query
-  ``title``: project title (default: ““)
-  ``description``: project description (default: ““)
-  ``image``: (optional) image ID
-  ``license``: (optional) license id (or multiple ids separated by
   commas) – if given, project will be created with this license
-  ``start``: start running the moment the project is created – uses
   more resources, but possibly better user experience (default: false)

Example:

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d title='MY NEW PROJECT' \
       -d description='sample project' \
       https://cocalc.com/api/v1/create_project
     == > {"event":"project_created",
           "id":"0b4df293-d518-45d0-8a3c-4281e501b85e",
           "project_id":"07897899-6bbb-4fbc-80a7-3586c43348d1"}

