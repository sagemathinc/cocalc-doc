.. index:: wysiwyg

========================
wysiwyg editing
========================

*What You See Is What You Get*

.. contents::
     :local:
     :depth: 1

.. epigraph::

    In computing, WYSIWYG ... is a system in which editing software allows content to be edited in a form that resembles its appearance when printed or displayed as a finished product

    -- Wikipedia

What You See Is What You Get editing. This feature is under development at present, but already quite usable. Select the "Editable" option in the pulldown menu at upper right.

To enable wysiwyg editing, select "Text" wherever 


#####################################
Where wysiwyg is Available in CoCalc
#####################################

* **Frame editor.**  With Markdown (.md) files. Select "Editable Text".

* **Chat.**

* **Whiteboard.** Text and sticky notes.

* **Jupyter notebooks.** Text or Markdown cell types.

########################
Features
########################

* **Real-time Collaboration.**

* **Markdown.**

* **LaTeX.**

* **Font options.** You can specify font family, face (bold, italics, etc.), size, and color.

If you select "Text" mode (instead of Markdown) for editing content between code cells,
then you can highlight any text and click the color palette icon, then set the color of that text.  This uses <span class='color:#0000ff'>...</span>
under the hood, as you can see by switching back to Markdown.  The format is sufficiently well defined that this doesn't get removed by our 
XSS processing, so it works even if your student opens the file and doesn't switch to trusted mode.

I also added some similar font face and font size menus, in case you want to use a different font ...




