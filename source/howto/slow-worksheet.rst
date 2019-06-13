.. index:: Sage Worksheets; slow
.. index:: Jupyter Notebooks; slow
.. _slow-worksheet:

================================================
Program Seems Slow or Stuck
================================================

**Question:** "Every time that I type a command into CoCalc, the server **does not work**. The green bar begins blinking but never evaluates the cell. The problem may happen with cells that worked before that suddenly start to stall. Sometimes the bar also blinks red. I have tried everything I could think of --
* logging out and back in
* refreshing the page
* checking my wifi connection
* restarting my computer, and
* closing and reopening the browser.

I'm not sure what else to try to get the server to work. It was working fine and then suddenly was not evaluating my cells."  (And, similar questions about Jupyter notebooks.)

**Answer:** There is no inherent problem. You can try several things.

.. index:: Member Hosting;slow worksheet

0. **Pay:** Use member hosting or dedicated CPU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are not a paying customer, `become one <https://cocalc.com/settings/billing>`_.  Make sure to buy a subscription (it is really affordable!) and upgrade your project so it runs on members-only hosts, increase your project RAM, etc.. You can also pay for dedicated CPU (a bit more expensive), to guarantee that your project runs quickly.

1. **Check Memory Use:** your project may be low on memory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :doc:`Low Memory Problems <low-memory>` for more information on how to detect and deal with low-memory situations.

2. **Restart:** in project settings, restart your project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This will stop any infinite loops you may have running in any worksheets, clear out any memory, etc. Just go to the "Settings" tab (wrench icon) of your project, then click "Restart project...".   If you have many worksheets or notebooks, running them consumes memory.

Don't worry. You will not delete anything when you restart your project.  The ONLY thing that is cleared is the state of variables or function definitions, so you may have to rerun some of your code. If you click on TimeTravel you can see that not only is nothing lost, and everything you've ever done is always saved.

3. **Reconnect:** Click on the network connection info at the top right
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can see if there are connection issues (outstanding messages being sent back and forth, etc.). If you click on reconnect you'll be randomly assigned to a different back-end web server, which may be less loaded.  You can also click refresh in your browse to just reload everything (without losing your place) from the same web server.

4. **Move:** Stop your project, then Start it again
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Several projects run on the same computer.  It's possible that your project is running on a computer that is very heavily loaded.  If you click the stop button in project settings, wait a minute until it completely stops, then start using your project again, it will be rescheduled to run on the least loaded node in the cluster.

5. **Kill:** Try to identify what is slowing your notebook or worksheet down and kill it
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open a terminal in your project (+New -> Terminal), then top `top` to see all processes that are running in your project.  Type `k` and enter a number from the left column to kill one of them.  `More help with top here... <https://alvinalexander.com/linux/unix-linux-top-command-cpu-memory>`_.

6. **Ask:** If nothing above works...
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If nothing above works, you may have hit a `bug in CoCalc <https://github.com/sagemathinc/cocalc/issues>`_.  Let us know so we can fix it by emailing help@cocalc.com and telling us as much as possible.

