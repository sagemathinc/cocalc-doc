======
stop
======


Use the ``stop`` endpoint to stop a CoCalc project, given its project_id. Note that this endpoint is in the ``v2/projects/`` subdirectory. The user must be signed in and must be an owner or collaborator on the project.

.. code:: bash

    x='sk_xxxxx' # your API key

    # project_id of the project you want to stop
    p='304506b4-262e-11ed-a279-2f22f36cbe91'

    curl -sk \
      -u $x: \
      -d project_id=$p \
      https://cocalc.com/api/v2/projects/stop

    ### project will be stopped; normal output is a pair of braces
    {}

You can learn more about the ``stop`` endpoint by viewing the source code at `https://github.com/sagemathinc/.../api/v2/projects/stop.ts <https://github.com/sagemathinc/cocalc/blob/master/src/packages/next/pages/api/v2/projects/stop.ts>`__.
