.. index:: Jupyter Notebooks; kernel terminated
.. _jupyter-kernel-terminated:

==================================================
Jupyter Kernel Terminated
==================================================

This page is may be helpful if you see the message:

   Kernel terminated -- this might be caused by running out of memory or hitting a bug in some library (e.g., forking too many processes, trying to access invalid memory, etc.). Consider restarting or upgrading your project or running the relevant code directly in a terminal to track down the cause.

###############################################
Is it caused by using up too much memory?
###############################################

Jupyter kernels terminating, and calculations failing that previously worked, can be a sign that your project is running low on memory.

Currently in CoCalc, if you open several Jupyter notebooks, they just sit there using memory. You have to explicitly :ref:`halt running notebooks <jupyter-halt>`, or kill them with ``top``, or restart your project in order for them to go away.  This can be a significant problem if you are grading a dozens of assignments.  You can see the cpu and memory usage of a Jupyter notebook in the upper right.

See :ref:`Low Memory Problems <low-memory>` for more information on how to detect and deal with low-memory situations.

###################################
Is it caused by something else?
###################################

It's possible, though by far the main source of trouble is lack of memory. If you suspect another problem, here are some things to try:

1. Try to eliminate Jupyter if possible
=======================================

Open a terminal, type e.g., ``anaconda3``, then copy and paste code in.

Or put the code in a ``.py`` file and import it.  CoCalc is also very good for editing ``.py`` files directly.

Does it segmentation fault or otherwise crash in a way that is very difficult for Jupyter to report? Of course, if so, we want to know -- help@cocalc.com.

2. Try to eliminate the CoCalc user interface
===============================================

Another thing you might try is to eliminate the CoCalc user interface to see what happens.  First, :ref:`close and halt <jupyter-halt>` your notebook in the CoCalc interface. Then go to project settings and launch the :ref:`Plain Jupyter Server <plain-jupyter-server>`.  You may have to refresh your browser after clicking.  Then navigate to your Jupyter notebook and open it.  If everything always works fine here, but not in CoCalc, there is some issue specifically with the CoCalc interface.  Let us know -- help@cocalc.com.
