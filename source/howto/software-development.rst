.. index:: Programming
.. index:: Software Development

======================================
Developing Software
======================================

This page is all about programming your own software (C, Fortran, Java, Julia, Octave, R, etc.) from CoCalc.
A highly related page is the FAQ for :doc:`Utilizing External Tools from CoCalc <external-tools>`.
There is also a separate page about :doc:`../jupyter` and :doc:`../sagews`.

.. note::

    If you don't find what you need, or if you'd like to ask a question, then please email `help@cocalc.com <mailto:help@cocalc.com>`_ at any time. We'd love to hear from you! Please include a link to any relevant project or document (copy and paste the URL address in your browser) as part of your email.

.. contents::
   :local:
   :depth: 2

General
===============================================================


Will my code keep running if I disconnect?
-------------------------------------------------

Even if my computer is put to sleep? Or do I need to have a machine open in order for the  process to run?

You definitely do not need to have your computer awake, or a window open, for your project to keep working. However, this is controlled by something called an "idle timeout," described in the next question.



.. index:: Idle Timeout; software development
.. index:: Timeout; idle
.. _idle-timeout:

What is an "idle timeout?"
-------------------------------

Under :doc:`../project-settings` (that's the wrench icon) there is an entry under
:ref:`project-upgrades` (left-hand side),
which will tell you how long the process will run "in the background."
There is an idle timeout for each project,
and it will be completely stopped (the technical term in UNIX is "killed") if you don't actively edit a file for that amount of time.

The default for free projects is 30 minutes.
You can increase this to 24 hours for only $14 per month.
This means that if you use your project a little bit once per day, then it will *never* timeout.

However, free projects have another limitation. A free project can be "killed" (stopped)
at any time, whatsoever. This will happen at least once per day. You have to keep this
in mind when designing your project. (For example, use checkpointing.) In contrast, all
paid projects are immune to this issue. See also :doc:`../upgrade-guide`.





Timeout/Killed calculations
---------------------------------

If I have code that has been running for a  while, and it times out or is otherwise "killed" (see previous question), what happens to the output?

If you are using a classical Jupyter notebook, then all output that is printed will be lost if no
browser is viewing it. This is a major design flaw in Jupyter. :doc:`CoCalc's Jupyter implemenetation <../jupyter>` behaves much better!

In contrast, Sage Worksheets will capture output even if no browser is observing them.

You can also (of course) write to a file on disk, which might be preferable in some cases.



Limitations of long-running computations
---------------------------------------------------

.. index:: Member Hosting;long-running computations

Open your project and click on Settings.
The default limitations are listed under "Quotas" in the lower left.
These can be raised, as mentioned there.  Notes:

* Projects without "member hosting" upgrade can get restarted regularly (these are hosted on Google preemptible instances).  You can check if a VM rebooted by typing "uptime".

* If a project isn't used (via the web-based UI) for the idle timeout (as listed in quotas), then all processes in that project are terminated and the user is removed (so ssh into the project also is not possible). You can :doc:`pay to raise <../upgrade-guide>` the idle timeout. See also :ref:`idle-timeout`.



See all processes running in my project
-------------------------------------------

See :ref:`htop`.

See Memory Usage
----------------------

See :ref:`smem`.


Is ``.bashrc`` or ``.bash_profile`` called on startup?
-------------------------------------------------------------

``~/.bashrc`` **is** run on startup and ``~/.bash_profile`` is **not**!
Hence, use ``~/.bashrc`` to customize your setup,
and you can also use ``~/.bash_aliases`` for your aliases (see ``~/.bashrc``).




Edit code and run a terminal side-by-side
----------------------------------------------

You can open up a terminal next to a code editor panel: :ref:`terminal-editor-panel`.



Sage Worksheets
=====================

Adjust the output cut-offs
---------------------------------------

It is an extremely common programming mistake to write an infinite loop, particularly when first learning about loops. Because CoCalc assumes an experienced programmer, the "cutoff limits" are set rather high. Users new to programming might want to set that limit lower, so that their screen isn't overflowing with repeated lines in the event that they inadvertently code up an infinite loop. (By the way, this works *in all languages*, not just Sage, e.g. R, C, FORTRAN, whatever you'd like.)

You can type::

    print sage_server.MAX_STDOUT_SIZE

at any time to find out the current limit. By default, it is 40,000.

Then, you can change it by typing something like this::

    sage_server.MAX_STDOUT_SIZE = 500

Note, this is 500 characters. Take care to ensure that the setting of this variable will be executed before your code starts. If you type

::

    sage_server.MAX_STDOUT_SIZE = 500

    for i in range(0,1000):
        print i

then it will be cut off somewhere in the middle of printing 152, because you need to count each digit, as well as the invisible "end of line" symbol. At the 501st character, the computation is stopped, and there is no more output.

By the way, it isn't just the case that the output is truncated at this point. The computation is halted as well. (The technical term for this is that "the process is killed.")


Fix an exception related to Sage's Integer(...) vs. Python ints?
---------------------------------------------------------------------

By default, Sage parses the input commands and replaces some elements with its own parts and also adds some syntactic sugar. For example, an integer like ``234`` is translated to ``Integer(234)`` in order to be more powerful and live as a part of Sage. To avoid this behaviour, either append an ``r`` to the number, like ``234r`` (the extra ``r`` tells Sage to consider this as "raw" input) or change the mode of the cell to Python by adding ``%python`` at the top. You can also switch to pure Python mode by default via ``%default_mode python``.   Alternatively, you can type ``Integer=int`` and possibly also ``RealNumber=float``.


Raise the limit on the number of output messages per cell
-------------------------------------------------------------

::

    import sage_server
    sage_server.MAX_OUTPUT_MESSAGES=100000

See `this published worksheet <https://cocalc.com/share/4a5f0542-5873-4eed-a85c-a18c706e8bcd/support/2014-11-01-155354-too-many-messages.sagews?viewer=share>`_ for more details.

Also, type ``sage_server.[tab key]`` to see information about other limitations.



Custom Modules
-------------------

Put an executable file with this content in ``$HOME/bin/sage``:

First, check where the global Sage install is by running ``which sage``. Most likely, it is at ``/ext/bin/sage``. Then create the file with the content::

    #!/usr/bin/env bash
    SAGE_PATH=$HOME/NEW_MODULE /ext/bin/sage "$@"

You could do this by making a new directory called bin, then a new file in there called "sage".
:doc:`In the terminal <../terminal>` type the following to make "sage" executable::

      cd; cd bin; chmod +x sage

Then restart the worksheet server by going project settings and clicking "Restart → Worksheet server".

Now any newly (re-)started worksheet will run with the above modified ``SAGE_PATH``.
Since ``SAGE_PATH`` is added to ``PYTHONPATH`` when Sage starts,
this does what you want.

(From Nathan Dunfield) Another approach, which also works now and doesn't require the custom ``$HOME/bin/sage``, is to use <http://docs.python.org/2/install/#alternate-installation-the-user-scheme>.

That is, one installs a module with ``sage -python setup.py install --user`` and it's dumped into

::

    $HOME/.local/lib/python2.7/site-packages

This location is searched automatically by Sage's Python without any intervention on the part of the user.
(However, you might have to restart the worksheet server to access newly installed modules from a worksheet.)
One can also put modules into the user's site-packages by hand and Sage will find them.


Julia in a Sage Worksheet
-----------------------------------


1. Click +New, type a filename, then click the "Sage Worksheet" button.

2. To evaluate code using Julia, begin the cell with ``%julia``, type the code, then press shift+enter.

3. Type ``%default_mode julia`` in a cell and press shift+enter; now all cells will be evaluated using Julia by default.  If you need to switch back, use ``%default_mode sage`` (or ``%sage`` to just switch back for one cell).


Detect Sage Worksheet Environment
----------------------------------------

If your code is running in a CoCalc worksheet, then the global variable ``__SAGEWS__`` will be defined.


Functions specific to Sage worksheets
-----------------------------------------

Type ``salvus.[tab key]`` to see the auto-complete list of functions or run ``dir(salvus)``.


Run Sage locally, on my own machine
--------------------------------------

There is a lovely tutorial on the web to help you do exactly that:
`Sage Installation Guide <https://doc.sagemath.org/html/en/installation/index.html>`_.


Custom Sage binaries
------------------------------------

See the instructions, :ref:`immediately below <custom-sage-build>`, on using a custom built-from-scratch copy of Sage. Just substitute your own ``.tar.gz`` file for the official build of Sage.


.. _custom-sage-build:

Custom built-from-source Sage
--------------------------------------

.. warning::

    This requires :doc:`a upgraded project <../upgrade-guide>` and takes **hours**!
    By default CoCalc projects have an idle timeout that is smaller. (see :ref:`idle-timeout`)
    If you aren't editing files in the project, your build will get killed part of the way through.
    If you're doing legit Sage development, email THE LINK TO YOUR PROJECT to help@cocalc.com
    and we will increase the idle timeout, disk space, RAM, etc, so you can contribute to Sage.

Open a :doc:`../terminal`.
Grab the source tarball (requires network access).
You can browse `files.sagemath.org <http://files.sagemath.org/>`_ to find recent releases and testing versions.

To build, do the following in your terminal (no need to worry about screen or tmux, of course, since sessions are persistent even if your browser leaves), and check back in a **few hours**::

    tar xvf sage-6.10.tar.gz && cd sage-6.10 && make

After doing that, do something like this in the terminal::

    cd; mkdir -p bin; cd bin; ln -s ~/sage-6.10/sage .

Then restart your worksheet server (in project settings).
Then for that project, you'll have your own 100% customizable copy of Sage; and moreover, when the system-wide Sage is upgraded, your project isn't impacted at all -- that sort of stability is a major win for some people.
This also uses little extra disk space in backups/snapshots, because of de-duplication.
You can of course also install any custom packages you want into this copy of Sage.
You can also help improve Sage: `Developer Guide <http://www.sagemath.org/doc/developer/>`_.

If you want to do Sage development see `How to develop for Sage using SageMath <http://mathandhats.blogspot.com/2014/06/how-to-develop-for-sage-using-sage-math.html>`_.

**Important:** Whenever you change Python code installed in that copy of Sage, you may have to restart the worksheet server and any running worksheets.  This is inconvenient, but is necessary because the worksheet server starts one copy of Sage, then *forks* off additional copies each time you open a new worksheet, which greatly reduces the time from when you open a worksheet until it actually starts computing things.

**Also Important:** If your copy of Sage is messed up in some way, then the worksheet server *can't* start, hence worksheets won't open.  To debug this, open a terminal and do this::

    ~$ cd .smc
    ~/.smc$ sage sage_server.py
    you should see an error here, e.g.,

and fix whatever error you see.  Also look at log files in ``~/.smc/sage_server/``




Python
==========

Custom Python3
-----------------

With full network access enabled, you can download and compile Python 3 this way.
Last line sets a symlink to make it your default!

::

    apt-get source python3.4-dev
    cd python3.4-3.4.0/
    ./configure --prefix=$HOME
    make
    make install
    cd ..
    pip3 install numpy
    pip3 install scipy
    pip3 install matplotlib
    pip3 install ipython
    pip3 install pyzmq
    pip3 install jinja2
    pip3 install tornado
    ln -s ~/bin/python3 ~/bin/python

How can I install Python packages from PyPI using pip?
----------------------------------------------------------

See :doc:`./install-python-lib`.




I would like to develop a webserver in Python
------------------------------------------------

See :doc:`./webserver`.

.. index:: Plotly
.. index:: Jupyter Notebooks; plotly

Run ``plotly`` in a Jupyter notebook
--------------------------------------------

You need to run `Plotly <https://plot.ly/>`_ plots in CoCalc under the **Plain Jupyter Server**.
For more information, see the :ref:`Jupyter Classic / Modern page <jupyter-classical-vs-cocalc>`.

Another option is to use the Plotly `Dash framework <https://plot.ly/products/dash/>`_:
here is a `working example running Dash from a CoCalc terminal <https://share.cocalc.com/share/db982efa-e439-4e2d-933b-7c7011c6b21a/DASH/dash-demo.py?viewer=share>`_



Install some software into my own Anaconda environment
-----------------------------------------------------------

See :ref:`anaconda-install`.

Configure a Jupyter kernel for my custom Anaconda environment
--------------------------------------------------------------------

See :ref:`anaconda-jupyter`.


R Statistical Software
=============================

I would like to install new R packages
--------------------------------------------

See :doc:`install-r-package`.



Process an R Markdown (.Rmd) documents
--------------------------------------------

See :ref:`edit-rmd`.



Use R in a Sage worksheet
---------------------------------------


1. Click +New, type a filename, then click the "Sage Worksheet" button.

2. To evaluate code using R, begin the cell with ``%r``, type the code, then press shift+enter.

3. Type ``%default_mode r`` in a cell and press shift+enter; now all cells will be evaluated using R by default.  If you need to switch back, use ``%default_mode sage``.

Override the default width and height for R SVG figures in a CoCalc worksheet
---------------------------------------------------------------------------------

To set width to 10 inches and height to 4 inches, use the sage command::

    r.set_plot_options(width=10, height=4)

If you have set default_mode to r, then enter the command in a sage mode cell::

    %sage r.set_plot_options(width=10, height=4)

You can change it by typing it again.

.. index:: Octave

Octave
=================

You can work with `Octave <https://www.gnu.org/software/octave/>`_ in

* Jupyter and CoCalc worksheets;
* run its graphical front-end in the :doc:`../x11`;
* work in a :doc:`../terminal`: add or use an existing "Terminal" file, ending in ``.term``,
  and type ``octave-cli`` on the command line;
* You can also create a file that ends with ``.m``, and edit it. 
  Then open an additional panel in the :doc:`../frame-editor` and change it to show a terminal and run the file right there.

Here are example Octave Jupyter notebook and an Octave CoCalc worksheets:

https://github.com/sagemathinc/cocalc-example-files/tree/master/octave

Other Languages
====================


Create, compile and run a C program
------------------------------------------------


1. Click +New, type a filename ending in ".c", e.g., ``foo.c``, and click "Create File" (or just press return).

2. Paste this code into the file::

    #include<stdio.h>
    int main(void) {
        printf("Hello World\n");
        printf("this is CoCalc!\n");
    }

3. Open a :doc:`../terminal` by clicking +New, clicking "Command Line Terminal" (or typing a filename ending in .term), and type ``gcc foo.c -o foo``.   Finally, run the program by typing ```./foo``.

Create, compile and run a Fortran F90 program
------------------------------------------------

See :doc:`./fortran`

Create, compile and run a Java program
------------------------------------------------


1. Create a file ``HelloWorld.java`` containing

::

    public class HelloWorld {
        public static void main (String[] args) {
            System.out.println ("Hello World!");
        }
    }

2. Create a terminal and run ``javac HelloWorld.java`` to compile your program.

3. Run ``java HelloWorld`` to see the output.

Create and run a Ruby program
------------------------------------------------

See :doc:`./ruby`


