import os
import sys
sys.path.insert(0, os.path.abspath('.'))

#---- Project information ------
project = 'Themis'
copyright =  '2020-2023, Themis developers'
author = 'Themis developers'

# The short X.Y version
version = ''
# The full version
release = ''

# -- General configuration ----
# Add any Sphinx extension module here, as strings.
extension = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewdoce',
]

# Usually you set "language" from command line for these cases.
language = 'en'


html_theme = 'furo'
html_static_path = ['_static']
html_logo = 'logo_themis.svg'
html_css_files = [
        'customize.css',
]

latex_engine = 'pdflatex'

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
}

# default
master_doc = 'index'
man_page = [
   (master_doc, project, '',
   [author], 1)
]

textinfo_documents = [
    (master_doc, project, '',
    author, 'themis developers', '',''),
]    
