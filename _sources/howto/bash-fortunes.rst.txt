.. index:: Bash Fortunes
.. _bash-fortunes:

===========================
Bash Fortunes
===========================

.. warning::

    This tutorial might be outdated!

.. note::

    This is user-contributed content. Credits go to Maxie D. Schmidt!

One of the most entertaining games available on a Unix / Linux system is the ``fortune`` command which prints random fortune cookies, or short messages, to the terminal. Many system administrators prefer to setup the ``fortune`` utility to print a new fortune every time a new terminal is opened. The printed fortunes can be customized further with the ``cowsay`` command which provides an ascii art figure speaking the fortune. We provide instructions for installing this ``fortune`` setup both on CoCalc and on a local Linux box in the next section. We also document the usage of the new ``math-fortune-mod`` add-ons available for download `here <https://github.com/maxieds/math-fortune-mod>`_.


Examples of the Fortune Command
========================================

The fortune command can be run by issuing the following at your terminal::

     $ /usr/games/fortune math.fortunes
     $ ls /usr/share/games/fortunes
     $ /usr/games/fortune debian

We can customize the printing of the fortunes with the ``cowsay`` command::

     $ /usr/games/fortune math.fortunes | /usr/games/cowsay -f Sigma
     $ ls /usr/share/cowsay/cows
     $ /usr/games/fortune debian | /usr/games/cowsay -f tux

The first and third of the previous commands should print output similar (though not identical) to the following ascii text::

     _______________________________________
     / TRIVIAL:                              \
     |                                       |
     | If I have to show you how to do this, |
     \ you're in the wrong class.            /
      ---------------------------------------
      \
        \
             -/////////////////:             
             +mMMMMMddddddddddMM             
              .omMMMh-``       +d             
                ``+dMMMy:``                    
                  ``/dMMMh/``                  
                    ``:hMMMd/                 
                      ``hMMh:                 
                    ``/hNh:``                  
                  ``/dNy-``                    
                ``+mMy-``       :s             
              ``omMMdsooooooooyNM             
             /mMMMMMMMMMMMMMMMMM             
             -::::::::::::::::::  

      _________________________________________
     / revision 1.17.2.7 date: 2001/05/31      \
     | 21:32:44; author: branden; state: Exp;  |
     | lines: +1 -1 ARRRRGH!! GOT THE G** D*** |
     \ SENSE OF A F******* TEST BACKWARDS!     /
      -----------------------------------------
        \
         \
             .--.
            |o_o |
            |:_/ |
           //   \ \
          (|     | )
         /'\_   _/``\
         \___)=(___/

Installation
=======================


Configuring the .bashrc File
-------------------------------------

If we desire to have a friendly bit of "mathy" wisdom printed out each time we open a bash terminal, either on the CoCalc or on our local box, we can append a ``fortune`` line to the end of the configuration file ``~/.bashrc``::

     $ echo -e "/usr/games/fortune math.fortunes | /usr/games/cowsay -f Sigma\n" >> ~/.bashrc
     $ source ~/.bashrc

If all went well in the installation, you should now have a Sigma-symbol-spoken math quote printed to the command line every time you open a new terminal. This behavior can be reversed by removing the corresponding ``fortune`` line at the end of ``~/.bashrc``.

Installing Packages on a Local Debian / Ubuntu Box
-------------------------------------------------------

CoCalc has both the ``fortune`` command, ``cowsay``, and the auxiliary math fortune packages installed for use in the CoCalc terminal applications. In order to get ``fortune`` and ``cowsay`` installed on your local Debian-based Linux box, we need to install a few packages with ``apt``::

     $ sudo apt-get install fortunes fortune-mod cowsay
     $ ls /usr/share/games/fortunes
     $ ls /usr/share/cowsay/cows

More ``fortune`` and ``cowsay``-related packages can be found by running the following search commands::

     $ apt-cache search fortune
     $ apt-cache search cowsay

In particular, we didn't install the offensive ``fortune`` and ``cowsay`` sets by default. Heed the warnings before you install these for use on your system: some of these fortune messages and quotes are truly offensive.

.. role:: strike

Next, we need to install the ``math.fortunes*`` fortune cookie messages and the ``Sigma.cow`` speaking Sigma symbol on the local system (again, CoCalc has these, :strike:`or will soon have these`, installed by default). We can install this extra data for use with ``fortune`` by running the next commands (if you do not have ``git`` installed, try running ``sudo apt-get install git-all`` first).

::

     $ cd ~
     $ git clone https://github.com/maxieds/math-fortune-mod.git
     $ cd math-fortune-mod/
     $ sudo cp math.fortunes{,.dat} /usr/share/games/fortunes/
     $ sudo cp Sigma.cow /usr/share/cowsay/cows/
     $ /usr/games/fortune math.fortunes | /usr/games/cowsay -f Sigma
