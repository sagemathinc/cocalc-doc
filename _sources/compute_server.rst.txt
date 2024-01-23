.. index:: Compute Servers
.. _compute-servers:

==========================
Compute Servers
==========================

.. contents::
   :local:
   :depth: 2
   
A compute server in CoCalc is a remote computer, whose resources (GPUs, CPUs, RAM, disks) you can utilize via CoCalc's collaborative interface in Jupyter notebooks and terminals. It is a way to open up possibilities for enhanced computing resources, extending far beyond the bounds of local machines.

To create a compute server, you select the software image, hardware and (optional) GPU, and can then start running any Jupyter notebook or Linux terminal on this server for an on-demand fee, charged by the second when the server is in use.

The GPU support is extensive, offering variants including A100 80GB, A100 40GB, L4, and T4 GPUs with finely configured software stacks. These stack images include SageMath, Google Colab, Julia, PyTorch, Tensorflow and CUDA Toolkit, accommodating a versatile range of uses. The compute servers come at highly competitive pricing, particularly for spot instances.

-------------------------------
Examples of Compute Server Uses
-------------------------------

You may find something useful, at least some inspiration, in our growing `collection of tutorials <https://github.com/sagemathinc/cocalc-howto/blob/main/README.md>`_ that make use of compute servers. You can either read them or follow along video versions. Here William explains how to run Google Colab environment on compute servers and use either Tensorflow or PyTorch:

.. raw:: html

    <center><iframe width="640" height="360" src="https://www.youtube.com/embed/kcxyShH3wYE?si=rGZEWZgs6XbOF38u" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></center>

----------------------------
Creating a Compute Server
----------------------------

Navigate to the project where you intend to use a compute server. Click on the "Servers" button on the left side of the screen and select "Create Compute Server":

.. figure:: img/compute_server_creating.png
    :width: 90%
    :align: center
    :alt: Creating a Compute Server

    Creating a Compute Server

You will be prompted to select the desired software image and optionally one or more GPUs.

If you are going to write code using CUDA libraries, choose the "Cuda Toolkit" image. If you want to accelerate PyTorch computations with a GPU, choose the "PyTorch" image. If you want to use SageMath, choose the "SageMath" image. Note that image selection does depend on the presence of a GPU.

Adjust the hardware parameters according to your needs. Take some time to look over the options! Note that you will be able to edit CPU and RAM when the machine if off, so if you don't quite know what you need - make a guess! If it turns out that you need something more or less powerful, you can easily make an adjustment. For example, in this video William uses a machine with 60 CPU cores and 240GB of RAM to build SageMath from source in under 18 minutes:

.. raw:: html

    <center><iframe width="640" height="360" src="https://www.youtube.com/embed/b8e8qq-KWbA?si=Y9N6ZtcVKo3fD9Fn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></center>

After the build is done, William changes the machine type to have only 2 CPU cores and 8GB of RAM - such a machine is very cheap to run even 24/7! The disk size can be increased even when the machine is running. Unfortunately, you currently can't move the machine from one region or zone to another unless it is deprovisioned, and the prices do depend on the region - this may change in the future.

Start your compute server!

------------------------------
Using a Compute Server
------------------------------

If you want to use the Linux command line, e.g., compilers, etc., create a terminal file (one ending in .term) and using the upper-left menu, select your compute server:

.. figure:: img/compute_server_terminal.png
    :width: 60%
    :align: center
    :alt: Connecting a Compute Server to a Terminal

    Connecting a Compute Server to a Terminal

If you chose the "CUDA Toolkit", then the "nvcc" command will be available for compiling .cu code. See `this tutorial <https://github.com/sagemathinc/cocalc-howto/blob/main/cuda.md>`_ for details.

When you edit files via CoCalc interface, they are synced to the compute server automatically. However, if you are using vim or some other tool in a terminal, you may need to click the "Sync" button at the top left for the files to get copied to your compute server:

.. figure:: img/compute_server_syncing.png
    :width: 60%
    :align: center
    :alt: Sync Button for a Compute Server

    Sync Button for a Compute Server

If you chose the "PyTorch" image or similar, create a Jupyter notebook and move it to the compute server via the upper-left menu in the same way. You can then select a Jupyter kernel that's available on the compute server, and your Jupyter notebook will run there:

.. figure:: img/compute_server_select_kernel.png
    :width: 90%
    :align: center
    :alt: Picking a Jupyter Kernel on a Compute Server

    Picking a Jupyter Kernel on a Compute Server

----------------------------
Billing for a Compute Server
----------------------------

A compute server is billed by the second and the price depends on its state:

- **Running** - the server is ready to perform your tasks, you pay for all of its resources and this is the price shown when creating a server
- **Suspended** - this is an analog of closing your laptop lid, you pay for the disk space and storing RAM state, but not for CPUs (compute servers with GPUs cannot be suspended)
- **Off** - this is an analog of shutting down your laptop, you pay only for the disk space and local data is available to you when you start the server again
- **Deprovisioned** - this is like writing down the model number of your laptop on paper, it costs nothing and when you start the server it will have the same characteristics, but all data that was not synced to your CoCalc project is gone.

In this example the running cost is $0.14/hour while the disk cost is less than a penny; notice the extra zero in $0.009/hour (that appears when you hover over the "Stop" button):

.. figure:: img/compute_server_cost_running_vs_stopped.png
    :width: 90%
    :align: center
    :alt: Compute Server Cost

    Compute Server Cost
