.. index:: Sage Worksheets; slow
.. index:: Jupyter Notebooks; slow
.. _slow-worksheet:

================================================
Program Seems Slow or Stuck
================================================

Here are some suggestions if CoCalc is responding slowly or stalls when you are typing into a program, whether it is a Jupyter notebook, a Linux terminal, a Sage worksheet, or other file.

.. contents::
   :local:
   :depth: 1

.. index:: Member Hosting;slow worksheet


Use member hosting or dedicated CPU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your project is running on a free trial server, it has limited resources.
:doc:`Paid licenses <../account/licenses>` are available.
Licenses allow you to add resources to your projects,
including *member hosting*, which moves them to less-loaded
members-only servers.

Try CoCalc Desktop
^^^^^^^^^^^^^^^^^^^^^

You can eliminate some browser-related problems by installing and running the :doc:`../cocalc-desktop` application. If the program no longer seems stuck, the cause is probably browser-related.

Debug the connection
^^^^^^^^^^^^^^^^^^^^^

Slow response and problems connecting have potential causes in common. You may find the solution to your issue in :doc:`connectivity-issues`.

Identify the problem program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Is there one specific file you work with that is much slower than others? If so, the problem is probably due to how that document or program is constructed, rather than a CoCalc platform issue.

If you're not sure whether some process in your project is slowing things down, you can use `top` or the :ref:`Process tab <ft-info>` for the project to find out.

To use `top`, open a terminal in your project (+New -> Terminal), then top `top` to see all processes that are running in your project.  Type `k` and enter a number from the left column to kill one of them.  `More help with top here... <https://alvinalexander.com/linux/unix-linux-top-command-cpu-memory>`_.

Check Memory Use
^^^^^^^^^^^^^^^^^^

Your project may be low on memory. 
See :doc:`Low Memory Problems <low-memory>` for more information on how to detect and deal with low-memory situations.

Restart the project
^^^^^^^^^^^^^^^^^^^^^

In project settings, restart your project. This will stop any infinite loops you may have running in any worksheets, clear out any memory, etc. Just go to the "Settings" tab (wrench icon) of your project, then click "Restart project...".   If you have many worksheets or notebooks, running them consumes memory.

You will not delete anything when you restart your project.  The ONLY thing that is cleared is the state of variables or function definitions, so you may have to rerun some of your code. If you click on TimeTravel, you can see that nothing lost, and everything you've done is saved.

Reboot
^^^^^^^^

Reboot your computer, then with nothing else running try using CoCalc. Your 
computer may be running other software that is competing with your
CoCalc session.


Reconnect
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on the network connection info at the top right.

You can see if there are connection issues (outstanding messages being sent back and forth, etc.). If you click on reconnect you'll be randomly assigned to a different back-end web server, which may be less loaded.  You can also click refresh in your browse to just reload everything (without losing your place) from the same web server.

Move
^^^^^^^^

Stop your project, then start it again. If you click the stop button in project settings, wait a minute until it completely stops, then start using your project again, it will be rescheduled to run on the least loaded node in the cluster.

If nothing works...
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If everything above fails, you need to tell us **exactly** what you're doing that is slow so that we can reproduce it. Otherwise, we won't be able to help. In particular,

#. What did you do exactly?

#. What happened?

#. How did this differ from what you expected?

If nothing above works, you may have hit a `bug in CoCalc <https://github.com/sagemathinc/cocalc/issues>`_.
Let us know so we can fix it by opening a support request using the :ref:`Help button <help-button>` at upper right. Opening a Help request when you have a problem file open in CoCalc causes a link to be included in the request, allowing our support team to find your project and file quickly.



