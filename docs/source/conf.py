# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup --------------------------------------------------------------
# If your Python source code is in a folder named `src` or something else,
# modify accordingly. For example:
# sys.path.insert(0, os.path.abspath('../src'))
# sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'smah'
copyright = '2024, Keith Brings'
author = 'Keith Brings'
release = '0.1.13'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',     # Auto-generate docs from docstrings
    'sphinx.ext.napoleon',    # Support for Google/NumPy style docstrings
    'sphinx.ext.viewcode',    # Add links to highlighted source code
    'sphinxcontrib.mermaid',  # Mermaid diagrams support
    'myst_parser',            # Markdown support via MyST
]

# MyST Parser settings
myst_enable_extensions = [
    'linkify',
    'substitution',
    'colon_fence',
    'deflist',
]
myst_fence_as_directive = ["mermaid"]

# Recognize both .rst and .md files as Sphinx sources
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Napoleon settings for docstring parsing
napoleon_google_docstring = True
napoleon_numpy_docstring = True

# autodoc options (use them if needed)
autodoc_default_options = {
    'members': True,
    'show-inheritance': True,
    'undoc-members': True,      # uncomment if you want to show undoc'ed members
    # 'private-members': True,    # uncomment if you want private members too
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# (Optional) If you want cross-project references, you can enable intersphinx:
# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3', None),
#     'sphinx': ('https://www.sphinx-doc.org/en/master', None),
# }

# -- Setup function (if needed) ----------------------------------------------
def setup(app):
    """Custom app setup if needed."""
    pass
