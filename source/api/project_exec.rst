project_exec
============

-  ``id``: A unique UUID for the query
-  ``project_id``: id of project where command is to be executed
   (required)
-  ``path``: path of working directory for the command (default: ““)
-  ``command``: command to be executed (required)
-  ``args``: command line options for the command (default: [])
-  ``timeout``: maximum allowed time, in seconds (default: 10)
-  ``aggregate``: If there are multiple attempts to run the given
   command with the same time, they are all aggregated and run only one
   time by the project; if requests comes in with a greater value (time,
   sequence number, etc.), they all run in another group after the first
   one finishes. Meant for compiling code on save.
-  ``max_output``: maximum number of characters in the output
-  ``bash``: if true, args are ignored and command is run as a bash
   command (default: false)
-  ``err_on_exit``: if exit code is nonzero send error return message
   instead of the usual output (default: true)

Execute a shell command in a given project.

Examples:

Simple built-in shell command.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d command=pwd \
       -d project_id=e49e86aa-192f-410b-8269-4b89fd934fba \
       https://cocalc.com/api/v1/project_exec
     ==> {"event":"project_exec_output",
          "id":"8a78a37d-b2fb-4e29-94ae-d66acdeac949",
          "stdout":"/projects/e49e86aa-192f-410b-8269-4b89fd934fba\n","stderr":"","exit_code":0}

Shell command with different working directory.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -d command=pwd \
       -d path=Private \
       -d project_id=e49e86aa-192f-410b-8269-4b89fd934fba \
       https://cocalc.com/api/v1/project_exec
     ==> {"event":"project_exec_output",
          "id":"8a78a37d-b2fb-4e29-94ae-d66acdeac949",
          "stdout":"/projects/e49e86aa-192f-410b-8269-4b89fd934fba/Private\n","stderr":"","exit_code":0}

Command line arguments specified by ‘args’ option. Note JSON format for
request parameters.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -H 'Content-Type: application/json' \
       -d '{"command":"echo","args":["xyz","abc"],"project_id":"e49e86aa-192f-410b-8269-4b89fd934fba"}' \
       https://cocalc.com/api/v1/project_exec
     ==> {"event":"project_exec_output",
          "id":"39289ba7-0333-48ad-984e-b25c8b8ffa0e",
          "stdout":"xyz abc\n",
          "stderr":"",
          "exit_code":0}

Limiting output of the command to 3 characters.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -H 'Content-Type: application/json' \
       -d '{"command":"echo","args":["xyz","abc"],"max_output":3,"project_id":"e49e86aa-192f-410b-8269-4b89fd934fba"}' \
       https://cocalc.com/api/v1/project_exec
     ==> {"event":"project_exec_output",
          "id":"02feab6c-a743-411a-afca-8a23b58988a9",
          "stdout":"xyz (truncated at 3 characters)",
          "stderr":"",
          "exit_code":0}

Setting a timeout for the command.

::

     curl -u sk_abcdefQWERTY090900000000: \
       -H 'Content-Type: application/json' \
       -d '{"command":"sleep 5","timeout":2,"project_id":"e49e86aa-192f-410b-8269-4b89fd934fba"}' \
       https://cocalc.com/api/v1/project_exec
     ==>  {"event":"error",
           "id":"86fea3f0-6a90-495b-a541-9c14a25fbe58",
           "error":"Error executing command 'sleep 5' with args '' -- killed command 'bash /tmp/f-11757-1677-8ei2z0.t4fex0qkt9', , "}

Notes: - Argument ``command`` may invoke an executable file or a
built-in shell command. It may include a path and command line
arguments. - If option ``args`` is provided, options must be sent as a
JSON object. - Argument ``path`` is optional. When provided, ``path`` is
relative to home directory in target project and specifies the working
directory in which the command will be run. - If the project is stopped
or archived, this API call will cause it to be started. Starting the
project can take several seconds. In this case, the call may return a
timeout error and will need to be repeated.

