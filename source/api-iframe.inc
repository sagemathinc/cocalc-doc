###########################
Using the API in an Iframe
###########################

Here are notes on integrating CoCalc in an iframe in a web application using the CoCalc API.
You should be able to create a proof of concept using the API introduction above and these notes.

#. You need an account with an API key. You can get an API key via the UI or here using the :doc:`create_account` API call.

#. You can create several accounts. If you are running the CoCalc Docker image, you probably want one account to be an `admin <https://github.com/sagemathinc/cocalc-docker#make-a-user-an-admin>`_ and then have additional accounts for each actual user of your platform.

#. You have to create projects. *Kubernetes note: In a kubernetes setup, each project runs in a pod with specific quotas. Collaborators on a project with upgrades or an administrator can set these quotas. If you're running several jupyter notebooks in the same project, they're running in the same pod. Depending on your use case, you might want to create a project for each notebook.*

#. With the API, you can :doc:`copy files between projects <copy_path_between_projects>` or :doc:`write to a file <write_text_file_to_project>`. It's also possible to :doc:`run arbitrary commands <project_exec>`.

#. To show a notebook to a user (and just the notebook) you need to do this

    * get a fresh auth token: https://doc.cocalc.com/api/user_auth.html
    * append the parameter fullscreen=kiosk to remove the UI
    * make an iframe in your website, which points to a project and file, and ends with ```?auth_token=...&fullscreen=kiosk```.

    A full example might look like this::

        https://cocalc.com/projects/....-....-....-..../
          files/calculate.ipynb?auth_token=......&fullscreen=kiosk&session=

There is work underway to improve kiosk mode. In particular to let the
parent website send commands to open more than one file, close them,
get status information, etc.
The PR is at https://github.com/sagemathinc/cocalc/pull/3985.
Once this is merged and working, the implication is that you just
have to open cocalc in kiosk mode::

    https://cocalc.com/app?auth_token=......&fullscreen=kiosk&session=

and wait until it is ready.
Then you can control opening and closing files from your website,
e.g. as a result of users clicking on certain buttons that behave
just like using the top row of cocalc.
