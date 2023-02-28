.. index:: Chat; chat rooms
.. _chatroom:

======================
Chatrooms
======================

CoCalc supports chatrooms for direct communication between collaborators
to enhance real-time collaboration on files.

.. contents::
     :local:
     :depth: 1

.. image:: img/chatroom.png
    :align: center
    :width: 95%
    :alt: two-person chat showing typeset integral

############
Features
############

* :ref:`chat-at-mentions`
* **Editing**: you can edit any message by double-clicking on it; a message specific "history" appears.
* **Emoticons**: a small set of characters are translated to unicode emoticons.
  E.g. type in ``:-)`` to express that you're happy!
* **Formulas**: You can write `LaTeX formulas`_ between `$` signs, e.g. ``$\frac{1}{x + \sin{x}^2}$`` renders as |FORMULA|.
* :ref:`chat-hashtags`
* **Insert images**: you can either upload and reference any files to be shown in a chat message,
  or drag'n'drop onto the input box to upload a picture. The file will be uploaded into a hidden directory with the name ``.chat-images`` and some appropriate HTML code will be inserted into the chat box.
* **Markdown**: Use `Markdown Syntax`_ to highlight ``**certain words**``, insert URL links, etc. See CoCalc :ref:`notes on markdown <cocalc-markdown-impl>` for implementation notes.
* **Notifications**: if there is any chat activity, the bell-icon at the top right will light up red and wiggle.
  Click on that bell to see where the activity is.
  You can click on the specific entry to open the file or chat,
  or click on the "Mark all read" button to clear the alert.
* **Search**: use the search box at the top left to filter messages. You can search for regular expressions by enclosing them in slashes, for example ``/^# /``.
* :ref:`side-chat`
* **Video chat**: the button named "Video Chat" opens up a 3rd party service,
  which establishes an audio and video connection for more in-depth discussions.

.. _Markdown Syntax: https://www.markdownguide.org/cheat-sheet/
.. _LaTeX formulas: https://en.wikibooks.org/wiki/LaTeX/Mathematics

.. |FORMULA| image:: img/chatroom-formula.png
                  :height: 20pt
                  :alt: typeset math formula

########################
Creating a Chatroom
########################

To start a new chat:

1. Open up the "Files" tab in a project;
2. (Maybe) switch to a specific directory, but any directory works;
3. Click the ``+ Add`` button and select the "Chatroom" filetype.

.. _chat-at-mentions:

########################
@-mentions
########################

Start a new word with the ``@`` symbol to create an ``@-mention`` in a chat message. A list of names appears and you can select one or more recipients of an email notification. Additional mentions of the same user will not trigger notifications for the next few hours, since we don't want to spam people. In order to send an email, CoCalc must have a working email address for the recipient.


.. figure:: img/teaching/tex-mentions.png
     :width: 90%
     :align: center
     :alt: @-mention causes email notifications to be sent

     @-mention of names in course shared project chat

You can see a list of all @-mentions sent to you by visiting the link https://cocalc.com/notifications

.. _chat-hashtags:

########################
Hashtags
########################

Put ``#tag`` anywhere in your chat message to add a hashtag. A hashtag begins with a pound sign ("#") and is followed immediately (no space after the "#") by any combination of letters, digits, and underscores. All hashtags used in the chat are displayed across the top of the chatroom. If you click one or more hashtags at the top, you see just the messages with those tags, and your message composer at the bottom will start with selected hashtag(s) to keep you in that thread. Delete hashtags in the message composer if you don't want them. Click on a hashtag that you previously selected at the top to turn off filtering for that tag. Precede a hashtag with a minus sign ("-") at the top to exclude messages with that tag.

Hashtags can also be used in CoCalc in :ref:`markdown files <markdown-hashtags>`, :ref:`project descriptions <project-desc-hashtags>`, and :ref:`whiteboards <whiteboard-hashtags>`.

.. index:: Side chat
.. index:: Chat; side chat
.. _side-chat:

########################
Side Chat
########################

At the top right in the Files toolbar for any open file, there is a chat icon: |comment-icon|.
This opens up a chatroom which is *specific to that file*.
This is commonly used to discuss the content of the given worksheet or notebook,
e.g. :ref:`students asking teachers/TAs <teaching-chatrooms>`.

.. image:: img/sagews-side-chat-a.png
    :align: center
    :width: 95%
    :alt: button at upper right and panel at right for side chat with a file




.. |comment-icon| image:: img/antd-icons/comment-icon.png
    :height: 20px
    :alt: comment or chat icon

