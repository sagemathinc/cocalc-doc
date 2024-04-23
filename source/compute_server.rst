.. index:: Compute Servers
.. _compute-servers:

Compute Servers
==========================

.. contents::
   :local:
   :depth: 2
   
A compute server in CoCalc is a remote computer, whose resources (GPUs, CPUs, RAM, disks) you can utilize via CoCalc's collaborative interface in Jupyter notebooks and terminals. It is a way to open up possibilities for enhanced computing resources, extending far beyond the bounds of local machines.

To create a compute server, you select the software image, hardware and (optional) GPU, and can then start running any Jupyter notebook or Linux terminal on this server for an on-demand fee, charged by the second when the server is in use.

The GPU support is extensive, offering variants including A100 80GB, A100 40GB, L4, and T4 GPUs with finely configured software stacks. These stack images include SageMath, Google Colab, Julia, PyTorch, Tensorflow and CUDA Toolkit, accommodating a versatile range of uses. The compute servers come at highly competitive pricing, particularly for spot instances.


Examples of Compute Server Uses
-------------------------------

You may find something useful, at least some inspiration, in our growing `collection of tutorials <https://github.com/sagemathinc/cocalc-howto/blob/main/README.md>`_ that make use of compute servers. You can either read them or follow along video versions. Here William explains how to run Google Colab environment on compute servers and use either Tensorflow or PyTorch:

.. raw:: html

    <center><iframe width="640" height="360" src="https://www.youtube.com/embed/kcxyShH3wYE?si=rGZEWZgs6XbOF38u" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></center>
    <br/>

Creating a Compute Server
----------------------------

There are multiple ways to create a compute server, one of them is to click the **Server** button:

.. figure:: img/compute_server_creating_2.png
    :width: 90%
    :align: center
    :alt: Creating a Compute Server

    Creating a Compute Server

The first settings allow you to give your server a name, pick a colour to easily distinguish where your are working, and choose the cloud provider used for your server:

.. figure:: img/compute_server_create_dialog.png
    :width: 90%
    :align: center
    :alt: Creating a Compute Server

    Creating a Compute Server

.. hint::

    You can actually be your own "cloud provider" by picking **On prem** hosting! You can use not only your own physical hardware, but also virtual machines from providers we are not currently integrated with. This is one of the ways we support :ref:`on-premises`. 
    
**Configuration** parameters vary depending on your hosting choice, but typically you can select the desired software image and hardware configuration including GPU(s).

If you are going to write code using CUDA libraries, choose the "Cuda Toolkit" image. If you want to accelerate PyTorch computations with a GPU, choose the "PyTorch" image. If you want to use SageMath, choose the "SageMath" image. Note that image selection does depend on the presence of a GPU.

Adjust the hardware parameters according to your needs. Take some time to look over the options! You will be able to edit CPU and RAM when the machine is off (if it also has a GPU, currently it will have to be deprovisioned), so if you don't quite know what you need - make a guess! If it turns out that you need something more or less powerful, you can easily make an adjustment. For example, in this video William uses a machine with 60 CPU cores and 240GB of RAM to build SageMath from source in under 18 minutes:

.. raw:: html

    <center><iframe width="640" height="360" src="https://www.youtube.com/embed/b8e8qq-KWbA?si=Y9N6ZtcVKo3fD9Fn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></center>

After the build is done, William changes the machine type to have only 2 CPU cores and 8GB of RAM - such a machine is very cheap to run even 24/7! The disk size can be increased even when the machine is running. Unfortunately, you currently can't move the machine from one region or zone to another unless it is deprovisioned, and the prices do depend on the region - this will change in the future.

Start your compute server!

Using a Compute Server
------------------------------

Your freshly created compute server does *not* replace your CoCalc project, but rather complements it. This is why you have to explicitly indicate that you want to run your terminal or Jupyter notebook on a particular compute server, and you can have multiple compute servers running at the same time!

.. hint::

    You can get close to a feeling of working "just on a compute server" if you switch to it in the file **Explorer** - you will be able to see its local files and all files that you open will run on the same compute server by default. See :ref:`compute-server-filesystem` below.

To run a Jupyter notebook on a compute server, click the **Server** button and select the one you want to use:

.. figure:: img/compute_server_notebook.png
    :width: 90%
    :align: center
    :alt: Connecting a Compute Server to a Notebook

    Connecting a Compute Server to a Notebook

You will get a confirmation dialog, reminding you that the current kernel will be stopped and a new one will have to be started on the compute server:

.. figure:: img/compute_server_confirmation.png
    :width: 90%
    :align: center
    :alt: Confirming the Choice of a Compute Server

    Confirming the Choice of a Compute Server

It is possible that the type of kernel used in your notebook is not available on the compute server (and vice versa). In this case you will need to choose another one:

.. figure:: img/compute_server_kernel.png
    :width: 90%
    :align: center
    :alt: Picking a Kernel on a Compute Server

    Picking a Kernel on a Compute Server


The server bar appearing above the notebook allows you to quickly see where the notebook is running and shows the name you have given to this server, its unique ID, and the image used. Click on this bar to see more details about the server:

.. figure:: img/compute_server_status.png
    :width: 90%
    :align: center
    :alt: Compute Server Status

    Compute Server Status

In order to use the Linux command line, e.g., compilers, etc., create a terminal file (one ending in .term) and connect it to a compute server in the same way. If you chose the "CUDA Toolkit" image, then the ``nvcc`` command will be available for compiling ``.cu`` code. See `this tutorial <https://github.com/sagemathinc/cocalc-howto/blob/main/cuda.md>`_ for details.


Becoming root and Port Forwarding
---------------------------------

You cannot become ``root`` or use ``sudo`` inside of a CoCalc project. If you try to, you will get a message like

.. figure:: img/no_sudo.png
    :width: 90%
    :align: center
    :alt: Error Message Using sudo

    Error Message Using sudo

On a compute server it is fully possible, just make sure that your terminal is running on a compute server as explained above:

.. figure:: img/compute_server_sudo.png
    :width: 90%
    :align: center
    :alt: Using sudo on a Compute Server

    Using sudo on a Compute Server

.. warning::
    Since you can do anything as ``root``, you may accidentally lose access to your compute server and your data. If this happens and you do need to regain access to data, contact support at help@cocalc.com
    
When you become ``root`` as above, you are still inside of a Docker container that is closely integrated with CoCalc. If this creates problems for your use case, you can escape from it and become ``root`` on the actual virtual machine that represents your compute server. To do this, :ref:`add SSH keys to your account <account-ssh>` (or project). Then use SSH to connect as ``root`` to ``localhost``:

.. figure:: img/compute_server_escape.png
    :width: 90%
    :align: center
    :alt: Escape from the Compute Server Container

    Escape from the Compute Server Container

Alternatively, you can use the external IP address of your compute server to connect to it from *any other machine*, bypassing CoCalc. This address is on the top of information about the server:

.. figure:: img/compute_server_direct_connect.png
    :width: 90%
    :align: center
    :alt: Compute Server IP Address

    Compute Server IP Address

The same address can be used to gain access to services. If any software on your compute server instructs you to "go to ``http://localhost:8123``", execute ::

    ssh -L 8123:localhost:8123 root@[server address]

on your *local* computer and go to ``http://localhost:8123`` in your *local* browser.


Billing for a Compute Server
----------------------------

A compute server is billed by the second and the price depends on its state:

- **Running** - the server is ready to perform your tasks, you pay for all of its resources and this is the price shown when creating a server
- **Suspended** - this is an analog of closing your laptop lid, you pay for the disk space and storing RAM state, but not for CPUs (compute servers with GPUs cannot be suspended)
- **Off** - this is an analog of shutting down your laptop, you pay only for the disk space and local data is available to you when you start the server again
- **Deprovisioned** - this is like writing down the model number of your laptop on paper, it costs nothing and when you start the server it will have the same characteristics, but all data that was not synced to your CoCalc project is gone.

.. warning::

    Please note that *there is* still a charge in the **Off** state! Namely the cost of the disk. Typically it is much less than the cost while **Running**, but it depends on your precise configuration.
    
.. hint::

    If you do not store local data on your server and do not customize the software environment, use the **Deprovisioned** state. You can make it the default using **Ephemeral Disk** setting in the server configuration.

In the example below the running cost is $0.30/hour while the disk cost is less than a penny! Notice the extra zero in $0.004 that appears when you hover over the **Stop** button (hovering over the cost per hour will also show the cost per month):

.. figure:: img/compute_server_cost.png
    :width: 90%
    :align: center
    :alt: Compute Server Cost

    Compute Server Cost


.. _compute-server-filesystem:

Compute Server Filesystem
-------------------------

In order to smoothly and successfully use a compute server, it is essential to understand how its filesystem interacts with your CoCalc project.

For the most part, all files in your CoCalc project conveniently appear in your home folder on the compute server and you can use them in a regular way. File changes inside of your CoCalc project and on your compute server can be synced both ways. This works great for Jupyter notebooks, for example. However, this convenience is still bound by laws of physics and because of network transfers involved it is much slower than modern local disks. You are also limited by your CoCalc disk quota.

If you need to read or write massive amounts of data, e.g. for data science or machine learning, or the programs you are running operate with a lot of files, e.g. ``git status`` with a large repository, you do need to use local fast directories on your compute server. These directories are configured in the compute server settings when you create or edit one:

.. figure:: img/compute_server_fast_data.png
    :width: 80%
    :align: center
    :alt: Fast Data Directories

    Fast Data Directories
    
As intended, these directories are *NOT* visible in your CoCalc project:

.. figure:: img/compute_server_project_files.png
    :width: 80%
    :align: center
    :alt: File Explorer on Project

    File Explorer on Project
    
In order to see them, to open files in them, or to open even synced files on the compute server without extra steps, connect your file explorer to the compute server in the same way as with notebooks and terminals, using the **Server** button. Now the fast data directories are visible (you can certainly have more than one):

.. figure:: img/compute_server_files.png
    :width: 80%
    :align: center
    :alt: File Explorer on Compute Server

    File Explorer on Compute Server
    

When you edit files via CoCalc graphical interface, they are usually synced between the project and the compute server automatically. However, if you are using ``vim`` or some other tool in a terminal, or just want the files to be synced immediately, you may need to click the **Sync Files** button:

.. figure:: img/compute_server_sync_files.png
    :width: 80%
    :align: center
    :alt: Sync Files Button for a Compute Server

    Sync Files Button for a Compute Server


.. _teaching_with_compute_servers:

Teaching with Compute Servers
----------------------------------

Compute servers are a great option to let your students or workshop participants use GPUs or powerful compute resources! Some important points to consider ahead of the course start:

- What configuration do you need for your students?

- How will you communicate it to them so that they don't miss important settings? (We do plan to support sharing server configuration directly, but it is not implemented yet.)

- Who will pay for running compute servers? The cost will be deducted directly from student accounts, but you can provide them with :ref:`credit-vouchers` if you wish, paying for those yourself.

- If you do use vouchers, you will need to figure out a suitable amount and, perhaps, develop a policy for those who run out of credit. For example, students may forget to turn off their servers when they are done working. It is also theoretically possible for them to configure a much more powerful machine than needed/instructed.

- Note that students can not spend more than they have in their account, so the worst case scenario is: they "burn" their allotment because of some mistake, put the same amount of money again, and hopefully behave in a more responsible manner the second time.

- For smaller courses it may be feasible for the instructor to create a server in each student project and allow collaborators (which includes students) to control it, i.e. they will be able to start and stop it:

  .. figure:: img/allow_collaborator_control.png
        :width: 80%
        :align: center
        :alt: Allow Collaborator Control

        Allow Collaborator Control

  In this case usage bills to the instructor account without any need for vouchers. Since the students can't edit the configuration of such a server, the worst case for an improper use is leaving the server running all the time.
























