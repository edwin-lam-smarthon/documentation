# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

project = 'Smarthon Smart Home Project'
copyright = '2024, Edwin Lam'
author = 'Edwin Lam'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

source_parsers = {
'.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']
extensions = [
'sphinx_markdown_tables',
'recommonmark'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# These folders are copied to the documentation's HTML output
html_static_path = ['_static']
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
'css/custom.css',
]
