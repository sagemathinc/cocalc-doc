================================
Project Initialization Scripts
================================

All about the **project-init.sh** file.

.. contents::
   :local:
   :depth: 1

While crontab-based management of periodic tasks is not available in CoCalc projects, we offer a flexible mechanism to use regular Bash, Python, or SageMath files for the same sort of capability.

************************
Project Initialization
************************

When a CoCalc project starts, an instance of `Supervisor <http://supervisord.org/>`_ is started and responsible for running:

* an instance of **"local hub"**. It is used for managing the project, communication with the outside world, monitoring, etc.
* **sshd**: the endpoint for remote SSH access.
* **initialization file**: an optional bash script called ``project_init.sh``, located in your home directory.

Initialization file management
==================================

Supervisor is configured to run this initialization file like background processes.
This means it checks the exit value of the process and restarts it if this code is not `0` or `2`.
Therefore, a script that runs without an error is **not** restarted.

On the other hand, if the process is terminated, interrupted or crashes – therefore the exit code is e.g. `1` – the process is restarted.
This adds some robustness to long running background jobs.

.. highlight:: sh

Example 1: record project start time
=====================================

A very simple example is to record the project's start time.
Go to your home directory and create a file `project_init.sh` with that content::

    date > project-start

This is a very simple bash script, which pipes the output of the `date` command into the file `project-start`.

.. highlight:: none

In order to see its effect, the file needs to be saved and the project restarted.
Give it a few seconds to come back online and run the script.
After that (maybe click the refresh button in the file listing) you should see this file and its content might look like::

    Mon Sep 12 11:14:20 UTC 2017

******************************
Other languages besides Bash?
******************************

You can run any language via bash's `exec`!
For example, `project_init.sh` containing::

    exec python3 project_init.py

will run a Python 3 initialization file named ``project_init.py``.


Example 2: a periodic task in Python
========================================

Here we write a small Python script,
which runs an infinite loop (*make sure to use `time.sleep`!*) and evaluates a function every 5 minutes.
This examples uses the library `schedule <https://schedule.readthedocs.io/en/stable/>`_.
Feel free to choose any other solution.

.. highlight:: python

1. ``project_init.sh``: contains ``exec python3 project_init.py``
2. The content of `project_init.py` is::

    import schedule
    import time
    from random import random
    from datetime import datetime

    i = 0

    def task():
        with open('task_output.log', 'a') as fout:
            ts = str(datetime.utcnow())
            fout.write("Task {}: {} value = {}\n".format(i, ts, random()))
            i += 1

    schedule.every(5).minutes.do(task)

    while True:
        schedule.run_pending()
        time.sleep(1)

.. highlight:: none

Indeed, after restarting the project the output of `ps auf` shows this "daemon" task as a child of supervisor::

    PID TTY      STAT   TIME COMMAND
      5 ?        Ss     0:01 /usr/bin/python /usr/bin/supervisord -c /cocalc/supervisor/supervisord.conf
     15 ?        Sl     0:01  \_ node /cocalc/src/smc-project/local_hub.js ....
     18 ?        S      0:00  \_ python3 /home/user/project_init.py
     ...

and the output file `task_output.log` contains::

    Task 0: 2017-09-12 12:02:22.636091 value = 0.12071154405652385
    Task 1: 2017-09-12 12:07:22.761420 value = 0.6513792691945387
    Task 2: 2017-09-12 12:12:22.891285 value = 0.5965113338132986
    ...

.. highlight:: python

Example 3: Periodic task in SageMath
=======================================

``run.sage`` is similar to the Python script above.

1. ``project_init.sh``: ``exec sage run.sage``
2. This results in Sage running a small task every two minutes and appends outputs to `sage_output.log`::

    import time
    from random import random
    from datetime import datetime

    i = 0
    def task():
        global i
        with open('sage_output.log', 'a') as fout:
            ts = str(datetime.utcnow())
            fout.write("Sage Task {}: {} value = {}\n".format(i, ts, random()))
            i += 1

    while True:
        task()
        time.sleep(2 * 60)

*************
Debugging
*************

To figure out why a script doesn't work as it should, there are two ways to debug it:

1. Run it directly in a terminal (create a ``*.term`` file) and run ``bash project_init.sh`` or ``python3 project_init.py``.
2. Check the logfile of Supervisor by running this in a terminal: ``cat /tmp/.cocalc/supervisord.log``.
   Among its logging there are likely entries hinting for exit states (e.g. ``INFO exited: project_init_sh (exit status 0; expected)``) or they show ``stdout``/``stderr`` output of the failed commands.
3. A common pitfall is to assume ``~/.bashrc`` is run.
   Since this is a non-interactive session, you need to explicitly source any additional environment information.

Note: much of this page is taken from the CoCalc blog article `Project Initialization Scripts <http://blog.sagemath.com/cocalc/2017/09/12/project-init.html>`_.