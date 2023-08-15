.. index:: Upgrades

=============================
Upgrades
=============================

.. contents::
   :local:
   :depth: 1

This article describes the different upgrades that are available for a CoCalc project.

After opening a project, you can view resource quotas for the project and add or remove licenses. Click "Upgrades" in the :doc:`activity-bar` for this feature.


.. figure:: img/upgrades.png
     :width: 100%
     :align: center
     :alt: upgrades pane

     upgrades pane

For billing information, see :ref:`upgrades-faq`.

.. _upg_mhost:

Member hosting
===============

There are two types of projects: "trial (free) projects" and "member projects".
:doc:`Trial projects <trial>` run on heavily loaded computers
sharing the same node with many other projects and system tasks.
These nodes might also shutdown at any time,
causing your currently running project to interrupt your work and restart.

Member-hosted projects are moved to less loaded machines,
which are reserved only for paying customers and aren't restarted on a daily basis.
The cluster scales up dynamically to accommodate for a varying number of member-projects.

Working in member-hosted projects feels much smoother because commands execute
more quickly with lower latency,
and CPU, memory and I/O heavy operations run more quickly.

.. _upg_net:

Internet access
===============

Despite the fact that you are accessing CoCalc through the internet,
you are actually working in a highly restricted environment.
Processes running *inside* a free project are not allowed to directly
access the internet. (We do not allow such access for free users, since when we did,
malicious users launched attacks on other computers from CoCalc.)

.. _upg_idleto:

Idle timeout
============

By default, free projects stop running after about 30 minutes of idle time.
This makes doing an overnight research computation –
e.g., searching for special prime numbers – impossible.

There is an advanced license option to prevent idle timeouts completely: see :ref:`licenses-always-running`.
Processes might still stop if they use too much memory, crash due to an exception, or if the server they are running on is rebooted.

Projects do not stop if you are continuously using them,
and there are no daily or monthly caps on how much you may use a CoCalc project, even a free one.

See also: :ref:`Software development/idle timeout <idle-timeout>`.

.. note::

    There is also a user-configurable timeout, the :ref:`standby-timeout`, which does not stop the project.

.. _upg_disk:

Disk space
==========

Disk space is the number of GB total used by your project's files. Snapshots and file edit history are included at no additional charge. Each project receives at least 3G of storage space. The maximum for typical CoCalc projects is 15GB of disk space. For even larger disk storage requirements, `dedicated disks <https://cocalc.com/store/dedicated?type=disk>`_ are available

.. _upg_ram:

RAM
======

The RAM quota limits the total amount of memory a project can use. The amount of RAM used by a running project will be the sum of RAM used by each of the collaborators. Therefore, the RAM quota will be larger if multiple collaborators are expected to use the project at the same time.

We recommend at least 2GB for general purposes. The maximum for typical CoCalc projects is 16GB of RAM. For even larger memory requirements, `dedicated VM's <https://cocalc.com/store/dedicated?type=vm>`_ are available.

.. _upg_cpu:

CPU
===

You can specify 1, 2, or 3 Shared CPUs, also known as Google Cloud vCPUs for a site license. To keep prices low, vCPUs may be shared with other projects, though member hosting very significantly reduces competition for CPUs.

To learn more about using more than one vCPU per project, see :doc:`howto/parallel`.

