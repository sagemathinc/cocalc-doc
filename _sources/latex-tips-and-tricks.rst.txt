.. index:: LaTeX Editor; tips and tricks

LaTeX Tips and Tricks
=====================

.. contents::
     :local:
     :depth: 1


.. index:: PythonTeX
.. _latex-pythontex:

PythonTeX
---------

.. raw:: html

    <center><iframe
        width="640" height="360"
        src="https://www.youtube.com/embed/sN--nWPyFuk?si=4y13tJQvRJsPrn26"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
    </iframe></center>
    
`PythonTeX <https://ctan.org/pkg/pythontex>`_ follows the same spirit as :ref:`latex-sagetex`.
Embedded Python commands and blocks of code are extracted into a ``.py`` file,
Python evaluates them,
and at the end the LaTeX engine merges the generated output snippets into the final document and renders the PDF file.
CoCalc handles all details for you!

To get going, insert ``\usepackage{pythontex}`` into the `preamble`_ of your document.
Then, you can insert inline code snippets via ``\py{}`` and blocks of code inside of ``\begin{pyblock}`` and ``\end{pyblock}``.
There is also support for `SymPy <https://www.sympy.org/>`_ code via ``\sympy{}`` or plots via Pylab using ``\pylab{}``.

For example, code like this::

    Python code: $2+3 = \py{2+3}$

    \begin{sympyblock}
    x = Symbol('x')
    f = x**2 * cos(x)
    fi = integrate(f, x)
    \end{sympyblock}

    The integral of $\sympy{f}$ is $\sympy{fi.simplify()}$

produces:

.. image:: img/latex-pythontex.png
    :width: 75%
    :align: center
    :alt: latex with pythontex


You can read more in the `PythonTeX Documentation <https://ctan.org/pkg/pythontex>`_.
Also note, that sometimes it is necessary to run build again to properly re-process all code snippets.
There is also a PythonTeX example document in the CoCalc Library.

.. _preamble: https://en.wikibooks.org/wiki/LaTeX/Document_Structure#Preamble


.. index:: SageTeX
.. _latex-sagetex:

SageTeX
-------

.. raw:: html

    <center><iframe
        width="640" height="360"
        src="https://www.youtube.com/embed/K-5CqXwRHgA?si=lX5bNDCtcUEoESFF"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
    </iframe></center>
    
Any ``.tex`` file loading the ``sagetex`` package is automatically processed via Sage.
First, Sage code is extracted into a ``.sage`` file, then ``sage ...`` evaluates that file, and finally the LaTeX engine creates the PDF document by replacing all snippets of Sage code by their evaluated result.
CoCalc handles all details for you!

To get going, you just have to insert ``\usepackage{sagetex}`` into the `preamble`_ of your document.
Calculations are done like that: ``$\frac{2}{3.5} = \sage{n(2/17)}$``, which results in |SAGETEX|.

See `SageTeX documentation <https://ctan.org/tex-archive/macros/latex/contrib/sagetex>`_ for more details and examples.
There is also a SageTeX example in the CoCalc Library.
Besides that, the `SageMath Documentation <http://doc.sagemath.org/html/en/>`_ could also be of help!

.. |SAGETEX| image:: img/latex-sagetex.png
                  :height: 17pt
                  :alt: sagetex


.. index:: Knitr
.. index:: Sweave
.. _latex-knitr:

Knitr
-----

`Knitr LaTeX documents`_ are different from SageTeX and PythonTeX.
They have their own filename extension (CoCalc supports ``.rnw`` and ``.Rtex``) and instead of calling LaTeX commands of a package, they feature their own syntax for embedded blocks and statements.
Historically, at first `Sweave`_ was added to R,
but Knitr is a much more modern variant with more features
(see `Transition from Sweave to Knitr`_). 

In general, the compilation works by first processing the input file via Knitr,
which runs R and generates a ``.tex`` document.
Then, the Latex engine processes that ``.tex`` file as usual.
CoCalc handles all details for you.

To get started, create a file ending with ``.rnw`` (Rweave/Sweave syntax) or ``.Rtex`` (code is in comment blocks).
Both will initialize the file with a template explaining you how to work with it.
For example, a block like::

    <<histogram-plot4, dev='tikz', fig.height=4, fig.width=10>>=
    data <- rnorm(1000)
    hist(data)
    @

produces a plot of a histogram, drawn using `TikZ`_.

.. image:: img/latex-knitr.png
    :width: 75%
    :align: center
    :alt: latex with knitr

Note that :ref:`latex-forward-inverse` will work as well as reporting errors.



.. index:: LaTeX Editor; build engine
.. _latex-build-engine:

Build Command
-------------

In the build panel, you can use the "Engine" dropdown menu to select a supported LaTeX engine.
This replaces the current build command with a generic one, that's know to work well in many situations!
These options are available:

* **latexmk** + **PDFlatex**: the default configuration, works in most cases
* **latexmk** + **XeLaTeX**: this is useful for foreign languages with many special characters.
* **latexmk** + **LuaTex**: uses the `LuaLaTeX <http://www.luatex.org>`_ engine.

**Output Directory**

By default, an ``-output-directory=...`` is set,
such that your current directory is kept clean of temporary files.
Instead, the actual build process happens in a temporary in-memory directory.

Some packages do not work under these circumstances,
hence there are ``(no bulid dir)`` variants, which do not set a temporary output directory flag.

**Bring your own command**

More general, you can also specify your own build command.
To avoid any processing of your build command, append a ";" semicolon at the end of your command or
even specify several commands separated by semicolons.
You could also use GNU Makefiles and call ``make ...;`` from here.

**Default build command**

The selected build command is stored in a companion file in the project, namely ``*.tex.syncdb``.
You can also store the default engine or even hardcode the build command in the LaTeX document itself.
There are two relevant directives, which are special comment lines at the beginning of your file.

1. ``% !TeX program = xelatex``: upon opening the file the first time, the ``XeLaTeX`` engine is selected. This is one of the default engine directives known from other latex editors. Later on, this line has no effect and your engine selection in CoCalc takes precedence. This could also be ``pdflatex`` or ``luatex``.
2. ``% !TeX cocalc = ... file.tex``: This takes precedence over any other build command configurations. The command after the equal sign is used to build your document. Without a semicolon, the last token is replaced by the current file name, hence it is ok to just add ``file.tex``. If there is a semicolon, no processing takes place. A suitable standard build command could be::

    % !TeX cocalc = latexmk -pdf -f -g -bibtex -deps -synctex=1 -interaction=nonstopmode file.tex

.. index:: LaTeX Editor; Gnuplot
.. index:: LaTeX Editor; shell-escape

Enable ``shell-escape``
-----------------------

There are situations where the LaTeX document calls certain utilities to accomplish a task.
One example is creating plots via `Gnuplot <http://www.gnuplot.info/>`_ right inside the document.

For example, a snippet of LaTeX code could look like this::

    \begin{figure}
      \begin{tikzpicture}
         \begin{axis}[ ... ]
           \addplot [...] gnuplot [raw gnuplot] {plot [-0.015:0.015] cos(380*x);};
         \end{axis}
      \end{tikzpicture}
    \end{figure}

In the middle, Gnuplot runs ``plot [-0.015:0.015] cos(380*x);`` to plot a cos function.

The *problem* is that by default the PDF LaTeX Engine doesn't allow to run arbitrary commands
due to security concerns. You'll see an error like that::

    Package pgfplots Error: Sorry, the gnuplot-result file 'gnuplot.pgf-plot.table'
    could not be found.
    Maybe you need to enable the shell-escape feature? [...]

.. note::

    You have to select the **PdfLaTeX (shell-escape)** engine from the selector for
    :ref:`latex-build-engine` or modify the build command manually.

As a result, Gnuplot will be run without errors. The necessary temporary files for the PGF plot will be created and the PDF will show the plot.
You can download the example :download:`gnuplot.tex <files/gnuplot.tex>` and see it in a screenshot below:

.. figure:: img/latex_shell_escape.png
  :width: 90%
  :align: center
  :alt: Shell Escape for gnuplot
  
  Shell Escape for gnuplot
  
 
.. index:: LaTeX Editor; texmf
.. index:: texmf

.. index:: LaTeX Editor; install packages
.. _install-latex-packages:

Install LaTeX Packages
----------------------

You can install LaTeX packages in your project:

#. Open a :doc:`terminal`
#. Check by running ``kpsewhich -var-value TEXMFHOME`` where you can install packages locally. It should tell you ``/home/user/texmf``.
#. Create the target directory based on the name of the package. E.g. if the package is called ``webquiz``, run ``mkdir -p /home/user/texmf/tex/latex/webquiz``.
#. Change your current directory to this one via ``cd /home/user/texmf/tex/latex/webquiz``.
#. Either download the package via ``wget ...`` from CRAN and extract it via ``tar xf <downloaded tarball>`` or ``unzip ...``. Alternatively, run ``open .`` to open this path in CoCalc's file explorer and use it to :ref:`upload <upload-files>` the style files there.

In any case, all files like ``*.sty`` and ``*.cls`` in that directory will be picked up when you load that package.
You can confirm that by searching for the style file, e.g. run ``kpsewhich [name.sty]``
and you should get a location like ``/home/user/texmf/tex/latex/.../[name.sty]``.

**Note** In case you use a zip file, place it in ``/home/user/texmf`` and run ``unzip [filename.zip]`` (or if there are already files, ``unzip -o [filename.zip]`` overwrites what's there).
It should extract into the correct subdirectories, in particular ``./tex/latex`` etc.

Use Your Own Styles
-------------------

If you want to make your custom style files available to all your ``.tex`` files (in a single project),
you have to put them into the ``~/texmf/tex/latex/local`` sub-directory. See `this StackExchange discussion <https://tex.stackexchange.com/questions/1137/where-do-i-place-my-own-sty-or-cls-files-to-make-them-available-to-all-my-te>`_ for more technical details.


.. index:: LaTeX Editor; add image

Include an Image
----------------

1. Upload a PNG or PDF file via CoCalc's "Files" interface.
   The uploaded image should be in the same directory as the ``.tex`` file
   Otherwise, use relative paths like ``./images/filename.png`` if it is in a subdirectory ``images``.
2. Add ``\usepackage{graphicx}`` to the preamble of your file, i.e. before ``\being{document``.
3. At the place where you want the image, insert a ``figure`` environment.
   Use ``includegraphics`` to include the file, with ``width`` to indicate image width, e.g. use ``0.9`` to take up 90% of document width.
4. Add ``\centering`` to have your image and caption centered in the document, and use ``caption`` to add a caption.

Here's the complete example:

.. code-block:: latex

    \usepackage{graphicx}
    ...
    \begin{document}
    ...
    \begin{figure}
    \centering
    \includegraphics[width=0.9\textwidth]{./images/filename.png}
    \caption{here is a picture}
    \end{figure}

5. There are many more options for image placement. See for example the Wikibooks LaTeX book section on 
   `Floats, Figures and Captions <https://en.wikibooks.org/wiki/LaTeX/Floats,_Figures_and_Captions>`_.




.. index:: LaTeX Editor; Asymptote
.. index:: Asymptote

Draw With Asymptote
-------------------

`Asymptote <http://asymptote.sourceforge.net/>`_ is a

    powerful descriptive vector graphics language
    that provides a natural coordinate-based framework for technical drawing.
    Labels and equations are typeset with LaTeX, for high-quality PostScript output.

In order to tell `LatexMK`_
– which CoCalc's LaTeX editor is using by default under the hood –
to process the generated ``*.asy`` files,
you need to setup your ``~/.latexmkrc`` file in your home directory.
In order to do that, open up the File Explorer in your project
and click on the home-icon to make sure you're in your home directory.
Then, click on **Create** to create a new file and enter the filename ``.latexmkrc``.
Don't overlook that leading dot in the filename, which is used for hidden files in Linux.
Then, enter these lines in the text editor and save the file::

    sub asy {return system("asy \"$_[0]\"");}
    add_cus_dep("asy","eps",0,"asy");
    add_cus_dep("asy","pdf",0,"asy");
    add_cus_dep("asy","tex",0,"asy");

These additional rules tell LatexMK to essentially run ``asy <basename>-*.asy``
on each file during the build process.
In case there are problems, you can run that command in a :doc:`terminal`
to see all details about any possible errors.

More information: `Asymptote LaTeX Usage <http://asymptote.sourceforge.net/doc/LaTeX-usage.html>`_.

.. image:: img/latex-asymptote.png
    :width: 100%
    :alt: latex with asymptote

.. index:: PSTricks
.. index:: LaTeX Editor; PSTricks

Use PSTricks Macros
-------------------

`PSTricks`_ is a set of macros for including PostScript drawings in a TeX document. The website has an extensive `gallery of examples`_.
The main thing to remember when using PSTricks is to set ``Engine`` in the CoCalc Build panel to ``XeLaTeX`` as in this small demo `.tex file`_ and `resulting .pdf`_.

.. _gallery of examples: http://tug.org/PSTricks/main.cgi?file=examples
.. _.tex file: https://cocalc.com/share/db982efa-e439-4e2d-933b-7c7011c6b21a/Public/pstricks-demo.tex?viewer=share
.. _resulting .pdf: https://cocalc.com/share/db982efa-e439-4e2d-933b-7c7011c6b21a/Public/pstricks-demo.pdf?viewer=share

.. image:: img/latex-pstricks-demo3.png
    :width: 40%
    :align: center
    :alt: pstricks demo part 1

.. image:: img/latex-pstricks-demo4.png
    :width: 40%
    :align: center
    :alt: pstricks demo part 2

.. index:: LaTeX Editor; embedding R/Python/Sage



.. _latex-word-count:

Word Count
----------

CoCalc can show you current word count statistics generated by texcount_.
In order to see them, change one of the frames or created a new one in the :doc:`Frame editor <frame-editor>`.
Select **"Word Count"** as shown below:

.. image:: img/latex-word-count.png
    :width: 50%
    :align: center
    :alt: latex word count

.. _texcount: http://app.uio.no/ifi/texcount/whatitdoes.html


Encoding
--------

All edited documents are assumed to be encoded as UTF-8 and modern LaTeX may work without explicitly specifying it, but some packages still require it. Depending on your build engine, the following encoding definitions are a good start:

* PDFLaTeX::

   \usepackage[T1]{fontenc}
   \usepackage[utf8]{inputenc}
   \usepackage{lmodern}

* XeLaTeX or LuaTeX::

   \usepackage{fontspec}



.. _Knitr LaTeX documents: https://yihui.name/knitr/
.. _Sweave: https://en.wikipedia.org/wiki/Sweave
.. _Transition from Sweave to Knitr: https://yihui.name/knitr/demo/sweave/
.. _TikZ: https://en.wikibooks.org/wiki/LaTeX/PGF/TikZ

.. _LatexMK: https://www.ctan.org/pkg/latexmk/
.. _subfiles: https://www.ctan.org/pkg/subfiles?lang=en
.. _CTAN subfiles: https://ctan.org/pkg/subfiles
.. _PSTricks: http://tug.org/PSTricks/main.cgi
