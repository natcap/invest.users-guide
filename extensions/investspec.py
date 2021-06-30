import docutils
import functools
import importlib


def format_basic_description(name, spec, indent):
    """Format the first line of the description for all input types.

    Args:
        name (str): Name of the input. Goes at the start of the line in bold.
        spec (dict): Arg dictionary or sub-dictionary from an ARGS_SPEC. Must
            have a 'type' key, and a 'units' key if the type is 'number'.
        indent (int): Number of tab characters to prepend to the line.

    Returns:
        RST-formatted string with the arg name, type, required status, units if
        applicable, and description.
    """
    # Represent the type as a user-readable string
    # a few types need a more user-friendly name
    # use :ref: to link them to the type description in input_types.rst
    if spec['type'] == 'freestyle_string':
        type_string = 'text_'
    elif spec['type'] == 'option_string':
        type_string = 'option_'
    elif spec['type'] == 'boolean':
        type_string = 'truefalse_'
    else:
        type_string = f'{spec["type"]}_'

    in_parentheses = [type_string]
    # For numbers, display the units
    if spec['type'] == 'number':
        as_str = unit_to_string(spec['units'])
        if as_str:
            in_parentheses.append(as_str)

    # Represent the required state as a string
    if 'required' not in spec or spec['required'] is True:
        # assume that it's required if it doesn't say otherwise
        required_string = 'required'
    elif spec['required'] is False:
        required_string = 'optional'
    elif isinstance(spec['required'], str):
        # assume that the about text will describe the conditional
        required_string = 'conditionally required'
    in_parentheses.append(required_string)

    # Nested arg components may not have an about section
    about_string = f": {spec['about']}" if 'about' in spec else ''

    return f"{indent}**{name}** ({', '.join(in_parentheses)}){about_string}"


def format_number_details(spec, indent):
    rst = ''
    if 'expression' in spec:
        rst += f'\t {indent}Constraints: {spec["expression"]}'
    return rst


def format_option_string_details(spec, indent):
    rst = f'| \t{indent}Options:'
    for option, about in spec['options'].items():
        rst += f'\n\n\t{indent}- {option}: {about}'
    return rst


def format_raster_details(spec, indent):
    rst = ''
    band = spec['bands'][1]
    if band['type'] == 'number':
        rst += f'\n\n\t{indent}units: {unit_to_string(band["units"])}'
    return rst


def format_vector_details(spec, indent):
    rst = f'\n\n\t{indent}Accepted geometries: {spec["geometries"]}'
    if spec['fields']:
        for field in spec['fields']:
            nested_spec = format_spec(
                field, spec['fields'][field], indent=indent + 1)
            rst += f'\n\n {nested_spec}'
    return rst


def format_csv_details(spec, indent):
    if 'columns' in spec:
        header_name = 'columns'
    elif 'rows' in spec:
        header_name = 'rows'
    else:
        header_name = None

    if header_name is None:
        rst = ' Please see the sample data table for details on the format.'
    else:
        rst = f'\n\n\t{indent}{header_name.capitalize()}:'
        for field in spec[header_name]:
            nested_spec = format_spec(
                field, spec[header_name][field], indent=indent + 1)
            rst += f'\n\n\t- {nested_spec}'
    return rst


def format_directory_details(spec, indent):
    rst = f'\n\n{indent}Contents:'
    for item in spec['contents']:
        nested_spec = format_spec(
            item, spec['contents'][item], indent=indent + 1)
        rst += f'\n\n- {nested_spec}'
    return rst


def format_spec(name, spec, indent=0):
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
        rst = format_basic_description(name, spec, indent)
        # Add details for types that have them
        if spec['type'] == 'number':
            rst += format_number_details(spec, indent)
        elif spec['type'] == 'option_string':
            rst += format_option_string_details(spec, indent)
        elif spec['type'] == 'raster':
            rst += format_raster_details(spec, indent)
        elif spec['type'] == 'vector':
            rst += format_vector_details(spec, indent)
        elif spec['type'] == 'csv':
            rst += format_csv_details(spec, indent)
        elif spec['type'] == 'directory' and 'contents' in spec and spec['contents']:
            rst += format_directory_details(spec, indent)

    # Dictionary components without the 'type' attr include
    # CSV rows/columns, directory contents, vector fields, raster bands
    elif isinstance(spec, dict):
        items = []
        for key, value in spec.items():
            nested_spec = format_spec(key, value)
            items.append(f'- {nested_spec}')
        rst = '\n\n'.join(items)
    # Display all other components as plain text
    else:
        rst = str(spec)

    return rst


def unit_to_string(unit):

    # pluralize the first unit so that it reads more naturally
    custom_unit_plurals = {
        'foot': 'feet',
        'degree_Celsius': 'degrees_Celsius'
    }
    as_str = str(unit)
    if as_str == 'none':
        return ''

    words = as_str.split(' ')
    first_unit = words[0]
    # check if it has an irregular plural form
    if first_unit in custom_unit_plurals:
        words[0] = custom_unit_plurals[first_unit]
    # for all others, add 's' to the end
    else:
        words[0] = words[0] + 's'
    as_str = ' '.join(words)
    # pint separates words with underscores
    as_str = as_str.replace('_', ' ')
    # represent exponents with a caret rather than asterisks
    as_str = as_str.replace(' ** ', '^')
    return as_str


def parse_rst(text):
    """Parses RST text into a list of docutils nodes.

    Args:
        text (str): RST-compatible text to parse

    Returns:
        list[docutils.Node]
    """

    doc = docutils.utils.new_document('',
                                      settings=docutils.frontend.OptionParser(
                                          components=(
                                              docutils.parsers.rst.Parser,)
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
    module = importlib.import_module(f'natcap.invest.{arguments[0]}')

    if len(arguments) == 1:
        args = module.ARGS_SPEC['args']
        rst = []
        for arg in args.values():
            text = format_spec(arg['name'], arg)
            rst += parse_rst(text)

    elif len(arguments) == 2:
        specs = arguments[1].split('.')

        # Get the dictionary value at the specified location in the module's spec
        value = functools.reduce(
            # recursively access nested dictionary values
            lambda dic, key: dic[key],
            specs,  # a list of nested dictionary keys
            module.ARGS_SPEC['args']  # the initial dictionary
        )
        # The last element of specs is the key name corresponding to `value`
        if 'name' in value:
            name = value['name']
        else:
            name = specs[-1]

        text = format_spec(name, value)
        rst = parse_rst(text)

    return rst, []


def setup(app):
    """Add the custom directive to Sphinx. Sphinx calls this when
    it runs conf.py which has `extensions = ['investspec']`"""

    app.add_role("investspec", invest_spec)

    return {}
