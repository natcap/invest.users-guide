import docutils
import functools
import importlib


def format_spec(name, spec):
    """Format an arg spec or subsection of an arg spec into text.
    
    Works for the entire args spec, or any nested dictionary within it (individual args or parts of args).
    This way, the generated content can be combined into the existing user's guide
    at whatever level makes sense for each situation.
    Args:
        name (str): Name to give the section. For top-level args this is arg['name'].
            For nested components it's typically their key in the containing dictionary.
        spec (dict): A dictionary that conforms to the InVEST args spec specification
    Returns:
        str
    """

    # Dictionaries that conform to the ARGS_SPEC component specification
    # can be formatted in a custom way
    if isinstance(spec, dict) and 'type' in spec:
        # Represent the required state as a string
        if 'required' not in spec:
            required_string = 'required'  # assume that it's required if it doesn't say otherwise
        elif spec['required'] is True:
            required_string = 'required'
        elif spec['required'] is False:
            required_string = 'optional'
        elif isinstance(spec['required'], str):
            required_string = f"required if {spec['required']}"

        # Represent the type as a user-readable string
        if spec['type'] == 'number':
            type_string = spec['units'] or 'number'
        elif spec['type'] == 'freestyle_string':
            type_string = 'text'
        elif spec['type'] == 'option_string':
            type_string = 'option'
        elif spec['type'] == 'boolean':
            type_string = 'true/false'
        else:
            type_string = spec['type']

        # Nested arg components may not have an about section
        about_string = f": {spec['about']}" if 'about' in spec else ''

        as_rst = f"**{name}** ({type_string}, {required_string}){about_string}"

        # Add details for types that have them
        if spec['type'] == 'option_string':
            as_rst += '\nOptions:'
            for option, about in spec['options'].items():
                as_rst += f"\n- {option}: {about}\n"

        elif spec['type'] == 'raster':
            as_rst += f'\n\nValues: code'

        elif spec['type'] == 'vector':
            as_rst += f'\n\nAccepted geometries: {spec["geometries"]}'
            if spec['fields']:
                for field in spec['fields']:
                    nested_spec = format_spec(field, spec['fields'][field])
                    as_rst += f'\n\n {nested_spec}'

        elif spec['type'] == 'csv':
            header_name = 'columns' if spec['columns'] else 'rows'
            if spec[header_name] is None:
                as_rst += '\nPlease see the sample data table for details on the format.'
            else:
                as_rst += f'\n\n{header_name.capitalize()}:'
                for field in spec[header_name]:
                    nested_spec = format_spec(field, spec[header_name][field])
                    as_rst += f'\n\n- {nested_spec}'

        elif spec['type'] == 'directory' and spec['contents']:
            as_rst += '\n\nContents:'
            for item in spec['contents']:
                nested_spec = format_spec(item, spec['contents'][item])
                as_rst += f'\n\n- {nested_spec}'

    # Dictionary components without the 'type' attr include
    # CSV rows/columns, directory contents, vector fields, raster bands
    elif isinstance(spec, dict):
        items = []
        for key, value in spec.items():
            nested_spec = format_spec(key, value)
            items.append(f'- {nested_spec}')
        as_rst = '\n\n'.join(items)
    # Display all other components as plain text
    else:
        as_rst = str(spec)

    return as_rst


def parse_rst(text):
    """Parses RST text into a list of docutils nodes.

    Args:
        text (str): RST-compatible text to parse

    Returns:
        list[docutils.Node]
    """
    doc = docutils.utils.new_document('',
        settings=docutils.frontend.OptionParser(
            components=(docutils.parsers.rst.Parser,)
        ).get_default_values())
    parser = docutils.parsers.rst.Parser()
    parser.parse(text, doc)

    # Exclude the all-encompassing document node
    top_node = doc.next_node()
    # This is a list of the node and its siblings
    return list(top_node.traverse(descend=False, siblings=True))


def invest_spec(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Custom docutils role to generate InVEST model input docs from spec.

    Docutils expects a function that accepts all of these args, even though
    only `text` is used right now.

    Args:
        name (str): the local name of the interpreted text role, the role name
            actually used in the document.
        rawtext (str): a string containing the entire interpreted text construct.
            Return it as a ``problematic`` node linked to a system message if
            there is a problem.
        text (str): the interpreted text content, with backslash escapes converted
            to nulls (``\x00``).
        lineno (int): the line number where the interpreted text beings.
        inliner (Inliner): the Inliner object that called the role function.
            It defines the following useful attributes: ``reporter``,
            ``problematic``, ``memo``, ``parent``, ``document``.
        options (dict): A dictionary of directive options for customization, to be
            interpreted by the role function.  Used for additional attributes for the
            generated elements and other functionality.
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
    arguments = text.split(' ')
    if len(arguments) != 2:
        raise ValueError(f'Expected 2 space-separated arguments but got {text}')

    module = importlib.import_module(f'natcap.invest.{arguments[0]}')
    specs = arguments[1].split('.')
    
    # Get the dictionary value at the specified location in the module's spec
    value = functools.reduce(
        lambda dic, key: dic[key],  # recursively access nested dictionary values
        specs,  # a list of nested dictionary keys
        module.ARGS_SPEC['args']  # the initial dictionary
    )

    # The last element of specs is the key name corresponding to `value` 
    text = format_spec(specs[-1], value)
    return parse_rst(text), []


def setup(app):
    """Add the custom directive to Sphinx. Sphinx calls this when
    it runs conf.py which has `extensions = ['helloworld']`"""

    app.add_role("investspec", invest_spec)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
