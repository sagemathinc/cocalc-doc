.. index:: wysiwyg

========================
WYSIWYG
========================

What-You-See-Is-What-You-Get editing.

.. epigraph::

    In computing, WYSIWYG ... is a system in which editing software allows content to be edited in a form that resembles its appearance when printed or displayed as a finished product

    -- Wikipedia

.. contents::
     :local:
     :depth: 1


#####################################
Where WYSIWYG is Available in CoCalc
#####################################

* :doc:`frame-editor`: when editing Markdown (.md) files. Select "Editable Text".

* :doc:`chat` as well as :ref:`side-chat`.

* :doc:`tasks`.

* :doc:`whiteboard` In text, sticky notes, and task lists.

* :doc:`jupyter` In text or Markdown cell types.

########################
Features
########################

* **Real-time Collaboration.**

* **Markdown.**

* **LaTeX.**

* **Font options.** You can specify font family, face (bold, italics, etc.), size, and color.

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


(Implementation note: WYSIWYG font options use <span class='color:#0000ff'>...</span>
under the hood.
The format is sufficiently well-defined that it doesn't get removed by CoCalc XSS processing. So it works even if e.g., a student opens the file and doesn't switch to trusted mode.)
