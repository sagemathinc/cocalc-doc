.. index:: Projects; low memory
.. index:: Memory; low
.. _low-memory:

==================================================
Low Memory Problems
==================================================

Why is my project out of memory?
----------------------------------------------------------

There are many possibilities.
All computer programs need to allocate memory in order to work – even the smallest ones could use a huge amount of memory!
Also, if you run several processes at the same time, their memory usage adds up.
All memory is finite and there are limits on each project to avoid that the server, where the project runs, to fill up and crash.

An **OOM: out-of-memory event** happens, when the sum of all memory usages of your project's processes exceeds the allowed quota or hits the limit of the host machine.
The Linux kernel (managing all processes) will switch into "survival mode" and attempt to get rid of large processes.
The selection is rather random, and will be recorded as part of the memory quota management of your project.
In case this happens, the only information is about *how many* processes were killed -- not which one in particular.

Usually this means you are running too many processes (too many :doc:`Sage Worksheets <../sagews>` or :doc:`Jupyter Notebooks <../jupyter>`).
Just closing the tab of their editor doesn't terminate them!

Alternatively, you might be running a single calculation that is using up too much memory (e.g. a large list, array or matrix, a heavy for-loop that appends data, etc.).
Please check your code to understand why this is happening.
Sometimes it's a small, innocent looking for loop that causes allocating too much memory!
For example::

    l = [1, 1]
    for i in l:
        l.append(l[-2] + l[-1])



Ways to clear up your project's memory
----------------------------------------------------------

**Jupyter**:

    * **Restart** the kernel
    * When you close it, click the :ref:`Halt button <jupyter-halt>`, which also terminates the kernel running your code behind the scenes. Just closing the tab does not stop it from running and it continues to be active in the background!

**Sage Worksheet**:

    * **Restart** the worksheet

**Entire Project** – if the above doesn't help or doesn't apply:

    * Make sure all your files are saved (disabled "Save" button resting idle)
    * Close all editor tabs, and **Restart the Project** (in Project Settings → Project Control). This will clean up all running processes and cleans up all state – all your files will still be there, of course.
    * Then only open up the file you want to work with!

    .. note::

        If there are collaborators on your project, they might start up additional notebooks. Check the project log if someone else is active at the same time.


Inspect in detail why the project is running out of memory
----------------------------------------------------------

1. Project settings
^^^^^^^^^^^^^^^^^^^

You can also look in the Settings (wrench) tab of your project under "Shared RAM", which will say how much is "currently" used.  This is only updated once every 30 seconds though, and may not show spikes in attempted memory allocation.

2. Use "top"/"htop" in a terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently the easiest way to test this is to open a terminal in your project, then type ``top``. Watch the processes listed there, especially the column labeled `RES`, which stands for "resident memory".
If your project has 1,000 MB of RAM, which is the default in CoCalc, and the sum of the RES entries is close to 1,000,000, then you should definitely expect a memory allocation failure soon.

You can type "M" into top to make it sort processes by memory, which will help in seeing how much is used.  You can also hit the space bar a lot to make it update frequently.  Type "q" when you are done.  If you want to kill a process in top, type "k" then the process id (PID), which is in the first column.

``htop`` is a more modern alternative to ``top``. You can use the functional keys to issue commands or even use the mouse to point and click.

3. Use "smem -ntk" in a terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command gives a useful breakdown of memory usage.

You may be able to work around a low-memory situation temporarily by killing selected processes or restarting your project.

But if you're hitting memory issues and just want more space, `upgrade your project <https://cocalc.com/settings/billing?session=default>`_.

The subscription are `listed here <https://cocalc.com/policies/pricing.html>`_. For example, for $14/month, you can upgrade memory from 1 GB to 5 GB, and have a **lot** more elbow room!  If you're confused or have questions about upgrading, just ask at help@cocalc.com.

4. Peak memory usage
^^^^^^^^^^^^^^^^^^^^^^^

In a :doc:`../terminal`, you can check the peak memory usage of a utility this way::

    $ /usr/bin/time -v [tool] [arguments]
    [...]
    Maximum resident set size (kbytes): ...



Software specific
-----------------

Grading Jupyter Notebooks
^^^^^^^^^^^^^^^^^^^^^^^^^

In case you're grading a bunch of Jupyter Notebooks, use the **"Halt" button** to not only hide the worksheet, but also terminate the associated kernel session. Also, avoid opening many of them at once in the same project!

Matplotlib
^^^^^^^^^^

When you produce many graphics in a row and use the usual *pyplot* API, the intermediate graphics are not cleaned up. Run the following to clear up the memory::

   import matplotlib.pyplot as plt
   plt.close('all')

RSTAN
^^^^^

In case you're using *rstan* in R, you can try to switch the C++ compiler to clang++. Run the following in a cell to create appropriate config files in your project::

    dir.create("~/.R", showWarnings = FALSE)
    cat("CXX = clang++",
        "CXXFLAGS = -g0 -Os -march=native -mtune=native",
        file = "~/.R/Makevars",
        sep = "\n")
    Sys.setenv(R_MAKEVARS_USER = normalizePath("~/.R/Makevars"))


Acknowledgment: `comment to CoCalc issue 2337 <https://github.com/sagemathinc/cocalc/issues/2337#issuecomment-355637033>`_ by @bgoodri.

