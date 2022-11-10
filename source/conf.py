import os
import sys
import subprocess
import setuptools_scm  # Just fail the process if this can't be found.

# add to the path so that sphinx can find our custom extension
sys.path.append(os.path.abspath('../extensions/investspec'))

# this is for the ReadTheDocs build, where conf.py is the only place we can
# run arbitrary commands such as checking out the sample data
subprocess.run(['make', '-C', '..', 'prep_sampledata'])

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx_reredirects',
    'investspec'
]

# config value for the investspec custom extension
# this is prefixed onto the :investspec: role's `module` argument before importing
# this way, we don't have to write 'natcap.invest' every time
investspec_module_prefix = 'natcap.invest'

# Enable figure number referencing with the :numref: syntax
numfig = True

gettext_compact = False

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'InVEST'
copyright = 'The Natural Capital Project'

# configure user-agent to avoid 403 errors on linkcheck
# https://github.com/sphinx-doc/sphinx/issues/7369
# This user agent string is coming from James' mac.
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0'

# this link has been unreliable but still seems to exist as of 3/2021. revisit in the future
linkcheck_ignore = [
    'http://trapdoor.bren.ucsb.edu/research/2014Group_Projects/documents/BermudaWind_Final_Report_2014-05-07.pdf']

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# If we're building the docs and have knowledge of the natcap.invest package,
# use the version string. If the version of natcap.invest cannot be found,
# raise an exception.
try:
    # If we're within an InVEST build context, use the InVEST version string.
    import subprocess
    version = subprocess.check_output(
        ['python', 'setup.py', '--version'], cwd='../../..').decode("ASCII")
    version = version.rstrip()  # remove the trailing newline

    # If in a development build, note that we're in an InVEST repo-managed version
    if 'post' in version:
        version = version.replace('+', '+invest.')
except subprocess.CalledProcessError:
    # If we're in a standalone build (like with the on-demand, always-updated
    # UG build), use the version string for the UG.
    version = setuptools_scm.get_version(
        version_scheme='post-release', local_scheme='node-and-date',
        root='..')

    # If not at a tag, note that we're in a UG repo-managed version
    if 'post' in version:
        version = version.replace('+', '+ug.')

# The full version, including alpha/beta/rc tags.
print(f'Version: {version}')

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# When a page is moved, redirect to the new page.
# Provided by the sphinx-reredirects extension.
redirects = {
    'reservoirhydropowerproduction': 'annual_water_yield.html',
}

# -- Options for HTML output --------------------------------------------------

# Alabaster is the default theme
html_theme = 'alabaster'

html_theme_options = {
    'analytics_id': 'UA-787904-8'
}

html_sidebars = {
    '**': [
        'about.html',
        'localtoc.html',
        'searchbox.html'
    ]
}

# Don't generate an index
html_use_index = False

# Don't generate a domain-specific index
html_domain_indices = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

html_static_path = ['custom.css']

# -- Internationalization options ---------------------------------------------
locale_dirs = ['locales/']
gettext_compact = False
