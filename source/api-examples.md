# API Examples & Howto

.. index:: pair: API; IFrame

## Embedding in an IFrame

Here are notes on integrating CoCalc in an IFrame in a web application using the CoCalc API.
You should be able to create a proof of concept using the API introduction above and these notes.

1. You need an account with an API key. You can get an API key via the UI or here using the :doc:`../api/create_account` API call.
2. You can create several accounts. If you are running the CoCalc Docker image, you probably want one account [to be an admin](https://github.com/sagemathinc/cocalc-docker#make-a-user-an-admin) and then have additional accounts for each actual user of your platform.
3. You have to create at least one project.
   Note: _The production website runs each project in their own container._
   _This means you might want to create several projects to get proper isolation._
4. With the API, you can :doc:`copy files between projects <../api/copy_path_between_projects>` or :doc:`write to a file <../api/write_text_file_to_project>`. It's also possible to :doc:`run arbitrary commands <../api/project_exec>`.
5. To show a notebook to a user (and just the notebook) you need to do this:
   - :doc:`get a fresh auth token <../api/user_auth>`
   - make an IFrame in your website, which points to a project and file, and ends with `?auth_token=...&fullscreen=kiosk`. The parameter `fullscreen=kiosk` removes the UI.
     A full example might look like this:
     ```
     https://cocalc.com/projects/....-....-....-..../
       files/calculate.ipynb?auth_token=......&fullscreen=kiosk&session=
     ```

There is work underway to improve kiosk mode.
In particular to let the parent website send commands to open more than one file, close them, get status information, etc.
The PR is at https://github.com/sagemathinc/cocalc/pull/3985.
Once this is merged and working, the implication is that you just have to open cocalc in kiosk mode:

```
https://cocalc.com/app?auth_token=......&fullscreen=kiosk&session=
```

and wait until it is ready.
Then you can control opening and closing files from your website,
e.g. as a result of users clicking on certain buttons that behave
just like using the top row of cocalc.
