.. index:: rich text

========================
Rich Text Editing
========================

*Rich text editing* refers to editing content in a form that resembles the final result, i.e. you are not interspersing formatting commands and text.

Here is how you would enter text in markdown code without rich text editing:

.. image:: img/not-rich.png
    :width: 50%
    :align: center
    :alt: markdown commands are displayed when not using rich text editing

Here is how the same content looks as you enter it with rich text editing:

.. image:: img/yes-rich.png
    :width: 50%
    :align: center
    :alt: rich text editing does not show formatting commands

In the example, you would type in the same characters in either case. With rich text editing enabled, you see the final result more clearly.

#####################################
Where Rich Text Editing is Available
#####################################

* :doc:`frame-editor`: when editing Markdown (.md) files. Select "Editable Text".

* :doc:`chat` as well as :ref:`side-chat`.

* :doc:`tasks`.

* :doc:`whiteboard` In text, sticky notes, and task lists.

* :doc:`jupyter` In text or Markdown cell types.

########################
Features
########################

"""""""""""""""""""""""
Real-time Collaboration
"""""""""""""""""""""""

Multiple users can use rich text editing on a file, and see one another's work at the same time.

"""""""""""""""""""""""
Markdown
"""""""""""""""""""""""

See :doc:`markdown`.

"""""""""""""""""""""""
LaTeX
"""""""""""""""""""""""

When using rich text editing, you can embed LaTeX directives between dollar signs ($) *followed by a space*. You must add a space to cause conversion to mathematical characters.

Here is an example of latex entry in :ref:`side-chat` for a file, before typing a space after the second $:

.. image:: img/rich-text-latex-1.png
    :width: 60%
    :align: center
    :alt: rich text editing with latex, before final space

Here is the formatting that results after typing the space:

.. image:: img/rich-text-latex-2.png
    :width: 60%
    :align: center
    :alt: rich text editing with latex, after final space


"""""""""""""""""""""""
Font options
"""""""""""""""""""""""

You can specify font family, face (bold, italics, etc.), size, and color.

If you select "Text" mode (instead of Markdown) for editing content between code cells,
then you can highlight any text and click the color palette icon, then set the color of that text.

For a markdown file: select "Editable Text" for font options.

.. image:: img/font-options-md.png
    :width: 60%
    :align: center
    :alt: font options while editing a .md file

For a Jupyter cell: select "Text" cell type, then "Edit" for font options.


.. image:: img/font-options-ipynb1.png
    :width: 60%
    :align: center
    :alt: font options while editing a .md file

.. image:: img/font-options-ipynb2.png
    :width: 60%
    :align: center
    :alt: font options while editing a .md file


(Implementation note: rich text font options use <span class='color:#0000ff'>...</span>
under the hood.
The format is sufficiently well-defined that it doesn't get removed by CoCalc XSS processing. So it works even if e.g., a student opens the file and doesn't switch to trusted mode.)