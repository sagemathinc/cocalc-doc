.. index:: Manage Processes

==============================
Manage Running Processes
==============================


.. index:: htop
.. _htop:

See all Processes
============================

Type exactly the following in a :doc:`../terminal` (+New → Terminal) to see all processes running in a project::

    htop

The header informs you about overall utilization of the node,
each row (you can scroll via your cursor keys) lists a process and use your F5 key
to toggle between a tree or a sorted list.
The column ``RES`` tells you the residual memory usage (what's really being used, more or less),
and the ``CPU%`` column the computational use of one CPU core.
The ``TIME+`` column tells you the aboslute time that process has used the CPU.

Select one or more processes via the space key of your keyboard.
Via the F9 key you can terminate or kill a process, etc.

If supported, mouse-clicks should also work.

See `htop manpage <http://linux.die.net/man/1/htop>`_ for more information.

.. image:: img/htop.png
    :width: 75%
    :align: center


.. index:: smem
.. _smem:

See Memory Usage
============================

Type exactly the following in a :doc:`../terminal` (+New → Terminal)::

    smem -tk

It lists all processes and the bottom line shows the total sum.
The last ``RSS`` column is probably the most interesting one, for more consult ``man smem``.   The total used memory is also listed under "Project usage and quotas" in :doc:`../project-settings` (based on Linux' cgroup management).
