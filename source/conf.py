# -*- coding: utf-8 -*-
#
# CoCalc Documentation documentation build configuration file, created by
# sphinx-quickstart on Tue Oct 30 10:39:09 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.insert(0, os.path.abspath('_ext'))  # or just '.'
from datetime import date

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    # 'edit_on_github',  # in _ext, but disabled/removed!
    'sphinx_sitemap'  # https://pypi.org/project/sphinx-sitemap/
]

html_baseurl = 'https://doc.cocalc.com/'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# edit_on_github custom extension config
edit_on_github_project = 'sagemathinc/cocalc-doc'
edit_on_github_branch = 'master'

# by default, we do not want any python parsing to happen
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-highlight_language
highlight_language = 'none'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:

source_suffix = ['.rst']

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'CoCalc Manual'
copyright = u'{}, Sagemath, Inc., CC BY-4.0 licensed'.format(date.today().year)
author = u'Sagemath, Inc.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
#release = f'{version}-{date.today().isoformat()}'
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['**/_*']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# 'alabaster' also works!
html_theme = os.environ.get('THEME', 'sphinx_rtd_theme')

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the documentation.

show_source = 'true'
html_show_sourcelink = False
html_favicon = 'img/favicon-32x32.png'
html_logo = 'img/cocalc-doc-logo.svg'
#GA_TAG = 'UA-34321400-6'

if html_theme == 'alabaster':

    # https://alabaster.readthedocs.io/en/latest/customization.html
    html_theme_options = {
        'description': 'CoCalc User Manual',
        'fixed_sidebar': 'false',
        'github_banner': 'false',  # we extend the theme's layout.html
        'github_user': 'sagemathinc',
        'github_repo': 'cocalc-doc',
        #'analytics_id': GA_TAG,
        #'sidebar_collapse': 'true',
        'show_powered_by': 'false',
        #'show_relbars': 'true', # doesn't work. not sure why.
        #'show_related': 'true', # doesn't make much sense, and also always points out the getting started page
        #'sidebar_collapse': 'true', # doesn't work, editing navigation.html directly
        'font_size': '11pt',
        'extra_nav_links': {
            'CoCalc': 'https://cocalc.com/',
            'Wiki': 'https://github.com/sagemathinc/cocalc/wiki'
        }
    }

elif html_theme == 'sphinx_rtd_theme':

    html_theme_options = {
        'canonical_url': 'https://doc.cocalc.com/',
        #'analytics_id': GA_TAG,  # this only works with the online version
        'logo_only': False,
        'prev_next_buttons_location': 'bottom',
        'style_external_links': False,
        # Toc options
        'collapse_navigation': True,
        'sticky_navigation': True,
        'navigation_depth': 4,
        'includehidden': True,
        'titles_only': False,
    }

    html_context = {
        # Add 'Edit on Github' link instead of 'View page source'
        # see https://github.com/rtfd/sphinx_rtd_theme/blob/master/sphinx_rtd_theme/breadcrumbs.html
        "display_github": True,
        'github_user': 'sagemathinc',
        'github_repo': 'cocalc-doc',
        'theme_vcs_pageview_mode': 'edit',
        'github_version': 'master',
        'conf_py_path': '/source/',
        'show_sphinx': False,
    }

    def setup(app):
        """
        Insert Google Analytics tracker
        Based on this Stackoverflow suggestion: https://stackoverflow.com/a/41885884
        """
        #app.add_js_file("https://www.googletagmanager.com/gtag/js?id={}".format(GA_TAG))
        ## this file is _static/google_analytics_tracker.js
        ## it also contains the GA_TAG !
        #app.add_js_file("google_analytics_tracker.js")
        # cocalc's analytics
        app.add_js_file("https://cocalc.com/analytics.js")

else:
    raise AssertionError(f'Unknown theme "{html_theme}"')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'CoCalcDoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        'CoCalc-Manual.tex',
        u'CoCalc Manual',
        u'Sagemath, Inc.',
        'manual',
    ),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'cocalc_doc', u'CoCalc Manual', [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        'CoCalcManual',
        u'CoCalc Manual',
        author,
        'CoCalcManual',
        'Manual for CoCalc',
        'Manual',
    ),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sage': ('https://doc.sagemath.org/html/en/reference', None),
}
