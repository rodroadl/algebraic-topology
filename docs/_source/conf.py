# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Algebraic Topology'
copyright = '2024, Allen Hatcher'
author = 'James Kim'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'hoverxref.extension'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# A list of CSS files. The entry must be a filename string or a tuple containing the filename string and the attributes dictionary. 
# The filename must be relative to the html_static_path, or a full URI with scheme like https://example.org/style.css. 
# The attributes is used for attributes of <link> tag. It defaults to an empty list.
html_css_files = ['custom.css']

# The “title” for HTML documentation generated with Sphinx’s own templates. 
# This is appended to the <title> tag of individual pages, and used in the navigation bar as the “topmost” element. 
# It defaults to '<project> v<revision> documentation'.
html_title = 'Algebraic Topology'



#LaTeX customization
#Unlike the HTML builders, the latex builder does not benefit from prepared themes. 
#The Options for LaTeX output, and particularly the latex_elements variable, provides much of the interface for customization. 
#For example:
latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
\usepackage{mathtools}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{relsize}
\usepackage{amsmath}
\usepackage{mathbbm}
\usepackage{xfrac}
\usepackage{dsfont}
\usepackage[titles]{tocloft}

\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex'
}
latex_show_urls = 'footnote'

# sphinx-hoverxref customization
# show a tooltip in all the appearances of the :ref: role
hoverxref_auto_ref = True
# To render a tooltip where its contents has a mathjax
hoverxref_mathjax = True