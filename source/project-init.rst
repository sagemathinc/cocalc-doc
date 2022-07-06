.. index:: crontab alternative

================================
Project Initialization Scripts
================================

All about the **project_init.sh** file.

.. contents::
   :local:
   :depth: 1

While crontab-based management of periodic tasks is not available in CoCalc projects, we offer a flexible mechanism to use regular Bash, Python, or SageMath files for the same sort of capability.

************************
Project Initialization
************************

When a CoCalc project starts this is run:

* an instance of **"local hub"**. It is used for managing the project, communication with the outside world, monitoring, etc.
* **sshd**: the endpoint for remote SSH access.
* **initialization file**: an *optional* bash script called ``project_init.sh``, located in the project's home directory. It is only started *once*!


.. highlight:: sh

Example 1: record project start time
=====================================

A very simple example is to record the project's start time.
Go to your project's home directory and create a file ``project_init.sh`` with that content::

    date > project-start

This is a very simple bash script, which pipes the output of the ``date`` command into the file ``project-start``.

.. highlight:: none

In order to see its effect, the file needs to be saved and the project restarted.
Give it a few seconds to come back online and run the script.
After that you should see this file and its content might look like::

    Mon Sep 12 11:14:20 UTC 2017

******************************
Other languages besides Bash?
******************************

You can run any language via bash's ``exec``!
For example, ``project_init.sh`` containing::

    exec python3 project_init.py

will run a Python 3 initialization file named ``project_init.py``.


.. index:: Periodic tasks

Example 2: a periodic task in Python
========================================

Here we write a small Python script,
which runs an infinite loop (make sure to use ``time.sleep``!)
and evaluates a function running a simple command every 10 minutes.
This examples uses the library `schedule <https://schedule.readthedocs.io/en/stable/>`_.
Feel free to choose any other solution.

.. highlight:: python

1. ``project_init.sh``: contains ``exec python3 project_init.py``
2. The content of `project_init.py` is::

    import schedule
    import time
    from datetime import datetime
    from subprocess import run, PIPE

    i = 0
    CMD = "date"

    def task():
        global i
        with open('task_output.log', 'a') as fout:
            ts = str(datetime.utcnow())
            status = run(CMD, stdout=PIPE, stderr=PIPE, shell=True)
            out = f"{status.stdout.decode('utf8')}\n{status.stderr.decode('utf8')}"
            fout.write("Task {}: {} output:\n{}\n".format(i, ts, out))
            i += 1


    schedule.every(10).minutes.do(task)

    while True:
        schedule.run_pending()
        time.sleep(60)


.. highlight:: none

Indeed, after restarting the project the output of `ps auxf` shows this task as a child of the project hub::

    USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    user           1  0.1  0.0   4520   756 ?        Ss   09:18   0:00 /cocalc/bin/tini -- sh -c env -i /cocalc/init/init.sh $COCALC_PROJECT_ID $KUCALC_IMAGE_NAME
    user           8  0.0  0.0   4628   832 ?        S    09:18   0:00 sh -c env -i /cocalc/init/init.sh $COCALC_PROJECT_ID $KUCALC_IMAGE_NAME
    user           9 10.7  0.4 978240 121400 ?       Sl   09:18   0:03  \_ node /cocalc/src/smc-project/local_hub.js --tcp_port 6000 --raw_port 6001 --kucalc
    user          21  0.0  0.0  72296  5728 ?        S    09:18   0:00      \_ /usr/sbin/sshd -D -p 2222 -h /tmp/.cocalc/ssh_host_rsa_key -o PidFile=/tmp/.cocalc/sshd.pid -f /cocalc/init/sshd_config
    user          22  0.5  0.0  37836 14332 ?        S    09:18   0:00      \_ python3 project_init.py
     ...

and the output file ``task_output.log`` contains entries for each run.

.. highlight:: python

Example 3: Periodic task in SageMath
=======================================

``run.sage`` is similar to the Python script above.

1. ``project_init.sh``: ``exec sage run.sage``
2. This results in Sage running a small task every two minutes and appends outputs to ``sage_output.log``::

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

To figure out why a script doesn't work as it should, check the output of the script:

* ``project_init.log`` contains the ``stdout`` output.
* ``project_init.err`` contains the ``stderr`` output, i.e. this will show any errors.

And please don't get confused, those files could contain stale information, because they aren't automatically deleted.

**************
Development
**************

#. It's highly recommended to start the bash script with ``set -e`` to stop at any errors and ``set -ev`` makes it more verbose as well.
#. Run it directly in a terminal (create a ``*.term`` file) and run ``bash project_init.sh`` or ``python3 project_init.py``.
#. A common pitfall is to assume ``~/.bashrc`` is run.
   Since this is a non-interactive session, you need to explicitly source any additional environment information.


.. note::

    Much of this page is taken from the CoCalc blog article `Project Initialization Scripts <http://blog.sagemath.com/cocalc/2017/09/12/project-init.html>`_.