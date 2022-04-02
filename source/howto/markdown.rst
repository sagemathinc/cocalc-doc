.. index:: markdown

========================
Markdown
========================

.. contents::
     :local:
     :depth: 1

########################
Introduction
########################

Wikipedia defines Markdown as "a lightweight markup language for creating formatted text using a plain-text editor" (`<https://en.wikipedia.org/wiki/Markdown>`_).

Markdown makes it easy to add basic structure, such as headings and lists, to a plaintext document. Use of Markdown is ubiquitous in CoCalc (see :ref:`below <where-markdown-used>`). When you start making notes into a text file, it is often most convenient to open the file as a Markdown document, i.e. a file with name ending in ".md". It is easy to produce pdf and html files from markdown.

There is a brief tutorial on Markdown in the :doc:`../project-library`. To copy the introduction into a project of yours, open the project and follow the four steps below:

.. image:: img/markdown-library-numbers.png
    :width: 100%
    :alt: fetching Markdown intro from the project library

The Library intro has three sample files, in format markdown (".md"), Jupyter notebook (".ipynb"), and Sage worksheet (".sagews"). Here's a view from the .md file:

.. image:: img/markdown-sample.png
    :width: 100%
    :alt: source and editable views of a .md file

You can find additional information about variations of markdown relevant to CoCalc at the following links:

* `Original markdown definition  <https://daringfireball.net/projects/markdown/>`_ by John Gruber. The basic features.

* `GitHub Flavored Markdown Spec <https://github.github.com/gfm/>`_. The customary format for README.md files, issues, and pull requests on GitHub.

* `Markdown Cells in Jupyter notebooks <https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html#Markdown-Cells>`_. Note that the CoCalc implementation of Jupyter notebooks is mostly compatible with this spec, with enhancements discussed below.

* `R Markdown <https://rmarkdown.rstudio.com/>`_. Geared toward data science, supports interleaving of executable code ("code chunks") in several programming languages, and documentation.

.. _where-markdown-used:

####################################
Where Markdown can be used in CoCalc
####################################

* Editing a ".md" file with the :ref:`frame editor <frame-editor-markdown>`
* :doc:`Chat rooms <../chat>` (".sage-chat" files)
* :ref:`Side chat <side-chat>` panel available with any file being edited
* :ref:`Text cells in Jupyter notebooks <cocalc-jupyter-features>`
* Markdown mode ("%md") in :ref:`Sage worksheets <what-is-sagews>`
* :ref:`R Markdown <edit-rmd>` (".Rmd" and ".rmd" files)
* :doc:`../tasks` (".tasks" files, also known as "Todo lists")

.. _cocalc-markdown-features:

###################################
Special features in CoCalc Markdown
###################################

* Embedded LaTeX. You can write `LaTeX formulas <https://en.wikibooks.org/wiki/LaTeX/Mathematics>`_ between ``$`` signs, e.g. ``$\frac{1}{1+x^2}$``.

* Emojis. View the list of supported emojis in the `markdown-it-emojis GitHub repository <https://github.com/markdown-it/markdown-it-emoji/blob/master/lib/data/full.json>`_.

* Checkboxes. Type " [ ] " to create an unchecked checkbox; " [x] " to create a checked box.

* Hashtags. Precede a word with a hash sign ("#") and it is formatted to stand out as a hashtag.

* @-mentions. See :ref:`@Mention collaborators in chat <at-mention-chat>`.

* WYSIWYG (what you see is what you get) editing. This feature is under development at present, but already quite usable. Select the "Editable" option in the pulldown menu at upper right.

* Inverse search in Markdown frame editor. The markdown editor supports **inverse search** when source and rendered views are both visible (this is the default display for markdown files). If you double-click on markdown in the rendered view, the source view will scroll to display the corresponding line.

* To export a markdown (".md") file as pdf, open the file, select "Locked" from the view pulldown menu and click the "Print" button.

* To create html from a markdown file, open a :doc:`Linux terminal <../terminal>`. If your file is "filename.md", run the command::

    pandoc filename.md -o filename.html


.. _cocalc-markdown-impl:

###########################################
About the CoCalc Implementation of Markdown
###########################################

CoCalc uses `markdown-it <https://github.com/markdown-it/markdown-it>`_, with plug-ins and some customizations. Details are in the CoCalc source code at GitHub in file `src/packages/frontend/markdown/index.ts <https://github.com/sagemathinc/cocalc/blob/master/src/packages/frontend/markdown/index.ts>`_.
