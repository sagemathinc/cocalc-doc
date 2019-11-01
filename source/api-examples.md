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
   - make an IFrame in your website, which points to a project and file, and ends with `?auth_token=...&fullscreen=kiosk`.
     The parameter `fullscreen=kiosk` removes the UI.
     A full example might look like this
     `https://cocalc.com/projects/.../files/calculate.ipynb?auth_token=...&fullscreen=kiosk&session=`

## IFrame communication

This is a communication channel to improve working with an embedded CoCalc instance.
It gives the parent page the ability to send command-messages to CoCalc (e.g. opening a specific page, etc.) and receiving responses.

The underlying technology is [window.postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage).

The parent page must be served using `https`!

.. note::

    This is *beta* and only available for specific domains.
    Please contact us if you want to use this.

To get started, you just have to embed the main `/app` endpoint in an IFrame's `src` like that:

```
https://cocalc.com/app?auth_token=......&fullscreen=kiosk&session=
```

Once CoCalc is ready, the loading screen shows a green banner of confirmation.

**Sending messages** Use [postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) on the `contentWindow` of CoCalc's IFrame to send messages.
E.g. if your IFrame has the `id="cocalc"`, run `cocalc = document.getElementById("cocalc").contentWindow;` and then `cocalc.postMessage(payload, "https://cocalc.com")`. `payload` is the message, which is explained below.

**Receiving message**

1. write a callback function like `function replies(mesg) { console.log(mesg.data); }`.
2. Possibly check if `mesg.origin` is really CoCalc's domain.
3. Hook up this callback via `window.addEventListener("message", replies, false);`.

**Messages sent to CoCalc** have the following structure. The `action` field is mandatory.

    {
      action: "[command]",
      field1: ...,
      field2: ...
    }

Each message has a **response**, usually containing `{status: "ack|done|error", ...}`.

In particular, **error responses** have the structure `{status: "error", mesg: "[error message]", ...}`.

Available commands and their responses:

- `open` – open a specific file in a project.
  - fields:
    - `project_id` – the UUID of the project
    - `path` – the location relative to the home directory. e.g. `notebook.ipynb` or `subdir1/file.md`.
  - responses:
    1. acknowledgement of command (project will start, file will open): `{ status: "ack", ... }`
    2. file editor is opened and loading of content starts: `{ status: "done", ... }`
- `closeall` – this closes all open files
  - response: `{status: "done", mesg: "all files are closed"}`
- `status` – returns a snapshot of CoCalc's overall status. In particular during starting CoCalc, querying this for a response is useful to know when CoCalc is available and connected to the front-end servers.
  - response:
    - `connection` – more detailed information about the connection quality, ping time, etc.
    - `open_files` – mapping of `project_id` to a list of paths.
