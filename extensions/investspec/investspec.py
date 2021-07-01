import docutils
import importlib

INPUT_TYPES_HTML_FILE = 'input_types.html'
# accepted geometries for a vector will be displayed in this order
GEOMETRY_ORDER = [
    'POINT',
    'MULTIPOINT',
    'LINESTRING',
    'MULTILINESTRING',
    'POLYGON',
    'MULTIPOLYGON']


def format_type_string(arg_type):
    # Represent the type as a string. Some need a more user-friendly name.
    # we can only use standard docutils features here, so no :ref:
    # this syntax works to link to a section in a different page, but it
    # isn't universally supported and depends on knowing the built page name.
    if arg_type == 'freestyle_string':
        return f'`text <{INPUT_TYPES_HTML_FILE}#text>`__'
    elif arg_type == 'option_string':
        return f'`option <{INPUT_TYPES_HTML_FILE}#option>`__'
    elif arg_type == 'boolean':
        return f'`true/false <{INPUT_TYPES_HTML_FILE}#truefalse>`__'
    else:
        return f'`{arg_type} <{INPUT_TYPES_HTML_FILE}#{arg_type}>`__'


def format_units_string(unit):
    # pluralize the first unit so that it reads more naturally
    custom_unit_plurals = {
        'foot': 'feet',
        'degree_Celsius': 'degrees_Celsius'
    }
    units_string = str(unit)
    if units_string == 'none':
        return ''

    words = units_string.split(' ')
    first_unit = words[0]
    # check if it has an irregular plural form
    if first_unit in custom_unit_plurals:
        words[0] = custom_unit_plurals[first_unit]
    # for all others, add 's' to the end
    else:
        words[0] = words[0] + 's'
    units_string = ' '.join(words)
    # pint separates words with underscores
    units_string = units_string.replace('_', ' ')
    # represent exponents with a caret rather than asterisks
    units_string = units_string.replace(' ** ', '^')
    # remove spaces around slashes
    units_string = units_string.replace(' / ', '/')
    return units_string


def format_required_string(required):
    if required is True:
        return 'required'
    elif required is False:
        return 'optional'
    else:
        # assume that the about text will describe the conditional
        return 'conditionally required'


def format_geometries_string(geometries):
    # sort the geometries so they always display in a consistent order
    sorted_geoms = sorted(
        list(geometries),
        key=lambda g: GEOMETRY_ORDER.index(g))
    return ', '.join(geom.lower() for geom in sorted_geoms)


def format_permissions_string(permissions):
    permissions_strings = []
    if 'r' in permissions:
        permissions_strings.append('read')
    if 'w' in permissions:
        permissions_strings.append('write')
    if 'x' in permissions:
        permissions_strings.append('execute')
    return ', '.join(permissions_strings)


def format_options_string(options, indent):
    # if the options don't have descriptions, display as a
    # comma separated list
    if isinstance(options, set):
        return ', '.join(sorted(list(options)))
    # if the options do have descriptions, display them as
    # a bulleted list
    elif isinstance(options, dict):
        lines = []
        sorted_options = sorted(list(options.keys()))
        for option in sorted_options:
            lines.append(f'{indent}- {option}: {options[option]}')

        return '\n\n'.join(lines)


def format_args_list(args, indent):
    items = []
    for arg_name, arg_spec in args.items():
        nested_spec = format_arg(arg_name, arg_spec, indent=indent)
        items.append(f'{indent}- {nested_spec}')
    return '\n\n'.join(items)


def format_arg(name, spec, indent):
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
    type_string = format_type_string(spec['type'])
    in_parentheses = [type_string]

    # For numbers and rasters that have them, display the units
    units = None
    if spec['type'] == 'number':
        units = spec['units']
    elif spec['type'] == 'raster' and spec['bands'][1]['type'] == 'number':
        units = spec['bands'][1]['units']
    if units:
        units_string = format_units_string(units)
        if units_string:
            in_parentheses.append(units_string)

    # Represent the required state as a string, defaulting to required
    if 'required' in spec:
        required_string = format_required_string(spec['required'])
    else:
        required_string = 'required'
    in_parentheses.append(required_string)

    # Nested args may not have an about section
    if 'about' in spec:
        about_string = f': {spec["about"]}'
    else:
        about_string = ''

    rst = f"{indent}**{name}** ({', '.join(in_parentheses)}){about_string}"

    # Add details for the types that have them
    if spec['type'] == 'option_string':
        rst += f'\n\n\t{indent}Options:'
        formatted_options = format_options_string(
            spec["options"], indent=indent+'\t')
        if isinstance(spec['options'], dict):
            rst += f'\n\n{formatted_options}'
        else:
            rst += f' {formatted_options}'

    elif spec['type'] == 'vector':
        rst += (f'\n\n\t{indent}Accepted geometries: '
                f'{format_geometries_string(spec["geometries"])}')
        if spec['fields']:
            rst += f'\n\n\t{indent}Fields:\n\n'
            rst += format_args_list(spec['fields'], indent=indent+'\t')

    elif spec['type'] == 'csv':
        if 'columns' in spec:
            header_name = 'columns'
        elif 'rows' in spec:
            header_name = 'rows'
        else:
            header_name = None

        if header_name is None:
            rst += ' Please see the sample data table for details on the format.'
        else:
            rst += f'\n\n\t{indent}{header_name.capitalize()}:\n\n'
            rst += format_args_list(spec[header_name], indent=indent+'\t')
        return rst

    elif spec['type'] == 'directory' and 'contents' in spec and spec['contents']:
        rst += f'\n\n\t{indent}Contents:\n\n'
        rst += format_args_list(spec['contents'], indent=indent+'\t')

    return rst


def parse_rst(text):
    """Parse RST text into a list of docutils nodes.

    Args:
        text (str): RST-formatted text to parse. May only use standard
            docutils features (no Sphinx roles etc)

    Returns:
        list[docutils.Node]
    """
    doc = docutils.utils.new_document(
        '',
        settings=docutils.frontend.OptionParser(
            components=(docutils.parsers.rst.Parser,)
        ).get_default_values())
    parser = docutils.parsers.rst.Parser()
    parser.parse(text, doc)

    # The content is wrapped in a paragraph node and the all-encompassing
    # document node. skip these so it can display in-line
    top_node = doc.next_node().next_node()

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

    def get_nested_key_value_pair(dic, keys):
        """
        """
        value = dic
        for key in keys.split('.'):
            try:
                value = value[int(key)]
            except ValueError:
                value = value[key]
        return key, value

    arguments = text.split(' ')
    prefix = inliner.document.settings.env.app.config.investspec_module_prefix
    if prefix:
        module_name = f'{prefix}.{arguments[0]}'
    else:
        module_name = arguments[0]
    module = importlib.import_module(module_name)
    args = module.ARGS_SPEC['args']

    if len(arguments) == 1:
        rst = format_args_list(args, indent='')

    elif len(arguments) == 2:

        # Get the dictionary value at the specified location in the module's spec
        key, value = get_nested_key_value_pair(
            module.ARGS_SPEC['args'], arguments[1])

        if key in {'units', 'projection_units'}:
            rst = format_units_string(value)
        elif key == 'type':
            rst = format_type_string(value)
        elif key == 'geometries':
            rst = format_geometries_string(value)
        elif key == 'permissions':
            rst = format_permissions_string(value)
        elif key in {'columns', 'rows', 'fields', 'contents'}:
            rst = format_args_list(value, indent='')
        elif key == 'options':
            rst = format_options_string(options, indent='')
        elif key in {'name', 'about', 'expression', 'regexp', 'projected',
                     'excel_ok', 'must_exist'}:
            # all the other
            rst = str(value)
        else:
            rst = format_arg(key, value, indent='')

    else:
        raise ValueError(
            f'Expected 1 or 2 space-separated args but got {text}')

    return parse_rst(rst), []


def setup(app):
    """Add the custom directive to Sphinx. Sphinx calls this when
    it runs conf.py which has `extensions = ['investspec']`"""
    # tell sphinx to get a config value called investspec_module_prefix from
    # conf.py. it defaults to an empty string.
    # its value will be accessible later in the invest_spec function.
    app.add_config_value('investspec_module_prefix', '', 'html')
    app.add_role("investspec", invest_spec)

    return {}
