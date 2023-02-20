.. index:: Slides

========================
Slides
========================

Give presentations with code and mathematics using `CoCalc Slides <https://cocalc.com/features/slides>`_.


pages view expands the page lets you delete drag pages around / overview can delete pages

You can create any number of slides. CoCalc slides let you use all the same tools as from the whiteboard: text, notes, freehand drawing, Jupyter code cells, mind maps, icons, and frames. Of course, text is editable in both markdown and rich text modes, with full latex formula and code block support.

Here's the CoCalc feature announcement and discussion: `ANN: CoCalc Slides -- create slides in CoCalc for presentations, with Jupyter code and latex math <https://github.com/sagemathinc/cocalc/discussions/6420>`_.

.. figure:: img/slides/slides.png
    :width: 100%
    :align: center
    :alt: example of CoCalc slides
    
    CoCalc Slides

.. contents::
     :local:
     :depth: 1

##############################
Chat
##############################

Chat with collaborators. Open multiple chat boxes in the document as well as the usual CoCalc :ref:`side-chat` for the entire slides file. Learn about CoCalc Chat at this link: :doc:`chat`.

Keyboard shortcut to create Chat boxes: "C".

.. figure:: img/whiteboard/chat.png
    :width: 90%
    :align: center
    :alt: example chat box and side chat

    chat box and side chat

##############################
Collaborative Editing
##############################

Many users can edit at the same time, see what the others are doing in real time, and center their view at the location of another's cursor.

##############################
Cut or Copy and Paste
##############################

Click "Select" (arrow icon) then drag the cursor to create a rectangular region. Doing so will select all objects that lie partially or completely in the region. "Cut" removes all the objects from their current position and saves them to the clipboard. "Copy" keeps the objects in their current position and saves them to the clipboard. "Paste" will drop the group of objects in the clipboard into the current page or into any page of any slides or whiteboard you have open.

.. figure:: img/whiteboard/cut-copy-paste.png
    :width: 70%
    :align: center
    :alt: select, cut or copy, and paste

    cut, copy, paste in whiteboard

Keyboard shortcut to enable rectangular selection: "V".

########################
Edges
########################

Create edges (arrows) between all objects.

Keyboard shortcut to create Edges: "E".

########################
Frames
########################

Use frames to group objects and organize a page into sections.

Keyboard shortcut to create a Frame: "F".


.. _slides-hashtags:

########################
Hashtags
########################

You can put hashtags on notes, e.g. :code:`#foo` and search for those as well, or put :code:`-` (minus sign) in front to exclude matching items from search, e.g. :code:`-#foo`. You can search for regular expressions by enclosing them in slashes, for example ``/^# /``.

########################
Icons
########################

Choose from a wide selection of Icons to add to your document.

Keyboard shortcut to open the table of available Icons: "I".


.. _slides-jupyter-cells:

##########################
Jupyter Cells
##########################

A CoCalc slides document can include Jupyter code cells. Code cells allow:

* over a dozen supported kernels
* CoCalc's massive library of pre-installed software
* interactive widgets
* execution order determined by a directed graph

.. image:: img/code-cells-in-wb.png
    :width: 80%
    :align: center
    :alt: slides with two code cells and a sticky note

Keyboard shortcut to create a Jupyter Code Cell: "J".

##############################
LaTeX Expressions
##############################

Text inside slides items supports LaTeX mathematical typesetting.

##############################
Navigate With Arrow Keys
##############################

While in Slides view, you can use the arrow keys: "↑" to move up one slide and "↓" to move down one slide from the current slide. Use Home (Fn–Left Arrow on some Mac keyboards) to go to the first slide and End (Fn–Right Arrow on some Mac keyboards) to go to the last slide.

.. _slides-pages-view:

##########################
Pages View
##########################

If you click the "Pages" icon: |pages-icon|, the Pages panel appears.

.. figure:: img/open-pages-view.png
    :width: 40%
    :align: center
    :alt: pages icon in toolbar

    pages icon in toolbar opens Pages view

There's a button "+ New" that creates a new page. You can see previews of all your pages in the pages panel, and click a preview to jump to any page.

You can also see a page number in upper left, and click or edit to go to a page.

.. figure:: img/page-one-of-two.png
    :width: 40%
    :align: center
    :alt: page number displayed at upper left

    slides is showing page 1 of 2

The Search panel is ordered by page number. Putting things in different pages imposes an ordering in the search.

##########################
Overview Map
##########################

Easily navigate with an overview map with two preview modes.


##########################
Pens
##########################

Choose one of the different pen shapes to draw freehand. Supported pointing devices include most forms of mouse and trackpad as well as many Wacom tablets and iPencil and Apple Pencil.

Keyboard shortcut to start using Pens: "P".

##########################
Publish
##########################

You can :ref:`publish <publishing-files>` your slides to the CoCalc share server.



.. _slides-search-view:

##########################
Search View
##########################

By default, the search panel is open to the right for new documents. You can also use the vertical toolbar at left and select the icon for the search panel: |search-icon|.

.. figure:: img/open-search-view.png
    :width: 40%
    :align: center
    :alt: search icon in toolbar

    search icon in toolbar opens Search view

*Search View* gives you a panel that lists all text, sticky notes and code in order, with a search box at the top. You can search for text and click on any matching item to center the view on it. The ordering of items in Search View is lexicographic by the \(y,x\) coordinates: items closer to the top are listed first; items at the same height are listed left to right.


Search view can make your slides documents easier to manage as they get larger.

.. figure:: img/wb-search-view.png
    :width: 100%
    :align: center
    :alt: example search view

    slides, showing search view in right panel

Search view works well with to-do lists. To find all not done items, put :code:`"[ ]"` (note the quotes) in the search box. To find all completed items, search for :code:`"[x]"`.

If you don't see a menu choice for Search View, then refresh your browser, click the "split vertically" button (upper right), then click the dropdown that says "Slides" and change it to "Search".

##############################
Split Windows
##############################

Infinitely split windows horizontally and vertically to view multiple parts of the document simultaneously.


##############################
Sticky Notes
##############################

A sticky note is a rectangle, with a colored background, for enclosing text. When creating a sticky note, it's easy to select from a variety of eye-catching background colors and text fonts and sizes.

Keyboard shortcut to create a Sticky Note: "N".

.. _slides-timers:

##############################
Stopwatches and Timers
##############################

Add stopwatches (count up) and timers (count down) to keep meetings and discussions on schedule.

.. figure:: img/whiteboard/timers.png
    :width: 50%
    :align: center
    :alt: stopwatches and timers

    stopwatches and timers in slides

Keyboard shortcut to create Stopwatches and Timers: "S".

When a timer counts down to zero, a pop-up announcement will be displayed if the slides file is open at the time.

.. figure:: img/whiteboard/wb-timer-expired.png
    :width: 50%
    :align: center
    :alt: timer expired pop-up

    notification displayed when slides timer expires


##############################
Table of Contents
##############################

You can view contents as an outline in a panel on the left and click to view any item instantly.

##############################
Text
##############################

A text box is a rectangle, with a transparent background, for enclosing text.

Keyboard shortcut to create a Text box: "T".

##############################
TimeTravel
##############################

As with other native CoCalc applications, every change is recorded via browsable :doc:`time-travel` You can see what changed, and who changed it, and copy/paste from any point in the history.


.. _slides-to-do-lists:

##########################
To-do Lists
##########################

In a sticky note, text, etc., you can mark action items by placing a pair of brackets in the item, preceded and followed by a space and with a space between the brackets. The item will be displayed with an empty checkbox. Click the checkbox when the item is done, or place an "x" between the brackets, and it will show as a checked item.

----

.. note::

    At this time, the only way to export an image slides document is by taking a screenshot. Exporting slides to a pdf, png, or svg file is not yet implemented. See `CoCalc issue #6024 <https://github.com/sagemathinc/cocalc/issues/6024>`_.


.. figure:: img/wb-tasks-code.png
    :width: 60%
    :align: center
    :alt: code for to-do list in a sticky note
    
    Code for an unchecked box and a checked box in a sticky note.

.. figure:: img/wb-tasks-rendered.png
    :width: 50%
    :align: center
    :alt: rendered list in a sticky note

    How the unchecked and checked boxes are displayed


.. |search-icon| image:: img/antd-icons/search-icon.png
    :height: 20px
    :alt: search icon

.. |pages-icon| image:: img/antd-icons/pages-icon.png
    :height: 20px
    :alt: pages icon

