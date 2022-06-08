
import importlib

from docutils import frontend
from docutils import nodes
from docutils import utils
from docutils.parsers import rst
from natcap.invest import set_locale
from natcap.invest import spec_utils


def parse_rst(text):
    """Parse RST text into a list of docutils nodes.

    Args:
        text (str): RST-formatted text to parse. May only use standard
            docutils features (no Sphinx roles etc)

    Returns:
        list[docutils.Node]
    """
    doc = utils.new_document(
        '',
        settings=frontend.OptionParser(
            components=(rst.Parser,)
        ).get_default_values())
    parser = rst.Parser()
    parser.parse(text, doc)

    # Skip the all-encompassing document node
    first_node = doc.next_node()
    number_of_top_level_nodes = len(
        first_node.traverse(descend=False, siblings=True))
    # if the content is wrapped in a paragraph node,
    # skip it so it can display in-line
    if (isinstance(first_node, nodes.paragraph) and
            number_of_top_level_nodes == 1):
        first_node = first_node.next_node()

    # This is a list of the node and its siblings
    return list(first_node.traverse(descend=False, siblings=True))


def invest_spec(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Custom docutils role to generate InVEST model input docs from spec.

    Docutils expects a function that accepts all of these args.

    Args:
        name (str): the local name of the interpreted text role, the role name
            actually used in the document.
        rawtext (str): a string containing the entire interpreted text
            construct. Return it as a ``problematic`` node linked to a system
            message if there is a problem.
        text (str): the interpreted text content, with backslash escapes
            converted to nulls (``\x00``).
        lineno (int): the line number where the interpreted text begins.
        inliner (Inliner): the Inliner object that called the role function.
            It defines the following useful attributes: ``reporter``,
            ``problematic``, ``memo``, ``parent``, ``document``.
        options (dict): A dictionary of directive options for customization, to
            be interpreted by the role function.  Used for additional
            attributes for the generated elements and other functionality.
        content (list[str]): the directive content for customization
            ("role" directive).  To be interpreted by the role function.

    Interpreted role functions return a tuple of two values:

    Returns:
        a tuple of two values:
            - A list of nodes which will be inserted into the document tree at
                the point where the interpreted role was encountered
            - A list of system messages, which will be inserted into the
                document tree immediately after the end of the current
                inline block.
    """
    # expect one or two space-separated arguments
    # the first argument is a module name to import (that has an ARGS_SPEC)
    # the second argument is a period-separated series of dictionary keys
    # that says what layer in the nested ARGS_SPEC dictionary to document
    arguments = text.split(' ', maxsplit=1)
    # access the `investspec_module_prefix` config setting from conf.py
    prefix = inliner.document.settings.env.app.config.investspec_module_prefix
    if prefix:
        module_name = f'{prefix}.{arguments[0]}'
    else:
        module_name = arguments[0]
    keys = arguments[1].split('.')  # period-separated series of keys

    # access the 'language' setting, and install it
    # before importing the desired invest module
    language = inliner.document.settings.env.app.config.language
    set_locale(language if language else 'en')

    spec_utils = importlib.import_module('natcap.invest.spec_utils')
    rst = spec_utils.describe_arg_from_name(module_name, *keys)
    return parse_rst(rst), []


def setup(app):
    """Add the custom extension to Sphinx.

    Sphinx calls this when it runs conf.py which contains
    `extensions = ['investspec']`

    Args:
        app (sphinx.application.Sphinx)

    Returns:
        empty dictionary
    """
    # tell sphinx to get a config value called investspec_module_prefix from
    # conf.py. it defaults to an empty string.
    # its value will be accessible later in the invest_spec function.
    app.add_config_value('investspec_module_prefix', '', 'html')
    app.add_role("investspec", invest_spec)
    return {}
