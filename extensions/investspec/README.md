# investspec extension for Sphinx

This is a custom Sphinx extension that generates documentation of InVEST model inputs from the model's `ARGS_SPEC`.
Its purpose is to help us reduce duplicated information and provide consistent, user-friendly documentation.
The `investspec` extension provides the `:investspec:` role, which can be used inline in RST files to insert generated documentation anywhere you want.

## Setup

`investspec` is already set up in the `conf.py` in this repo.

In case we need to use it anywhere else, here's how to set it up:
In the `conf.py` file for the source RST, add the `investspec/` root directory to `sys.path` so that Sphinx can find it:
```
sys.path.append(os.path.abspath('../extensions/investspec'))  # or other path as appropriate
```
and add `investspec` to the list of extensions:
```
extensions = ['investspec']
```
to avoid writing out `natcap.invest. ...` before the module name every time, set the module prefix:
```
investspec_module_prefix = 'natcap.invest'
```

## Usage

The `investspec` role can take one or two arguments: `` :investspec:`module` `` or `` :investspec:`module key` ``.

`module` (or `f'{investspec_module_prefix}.{module}'` if `investspec_module_prefix` is defined) must be an importable python module. It must have an attribute `ARGS_SPEC` that is a well-formed InVEST args spec dictionary. If there is only one argument, documentation is generated for all the args (everything under `ARGS_SPEC.args`).

The optional second argument allows you to generate documentation for a specific arg or nested arg attribute. It is a period-separated series of dictionary keys accessed starting at `ARGS_SPEC.args`. For example, here's an excerpt from the Forest Carbon spec, located at `natcap.invest.forest_carbon_edge_effect`:
```
ARGS_SPEC = {
    "model_name": "Forest Carbon Edge Effect Model",
    "args": {
        "biophysical_table_path": {
            "type": "csv",
            "name": "Biophysical Table"
            "columns": {
                "lucode": {"type": "code"},
                "is_tropical_forest": {"type": "boolean"},
                "c_above": {
                    "type": "number",
                    "units": ureg.metric_ton/ureg.hectare,
                    "about": (
                        "Carbon density value for the aboveground carbon "
                        "pool.")
                },

...
}
```
- `` :investspec:`forest_carbon_edge_effect` `` will generate a bulleted list of descriptions of each arg.

- `` :investspec:`forest_carbon_edge_effect biophysical_table_path` `` will generate a description of the biophysical table arg, titled `Biophysical Table`. It will include a bulleted list of descriptions for each column.

- `` :investspec:`forest_carbon_edge_effect biophysical_table_path.columns` `` will generate a bulleted list of descriptions of each column in the table.

- `` :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_above` `` will generate a description of only the `c_above` column.

- `` :investspec:`forest_carbon_edge_effect biophysical_table_path.columns.c_above.units` `` will generate a human-readable units phrase e.g. `metric tons/hectare`

You can access any value in the `ARGS_SPEC.args` dictionary this way. Most types/attributes generate docs in a custom format. Anything else is represented with `str(value)`.

## What is documented

## What is not documented
- `expression`s for `number` types. This can be any python expression, so it may be too complicated to to auto-format into human readable text. Any limits on a `number`'s value should also be described in the `about` text.
- Conditional requirements (`"required": <str>`). This can be any python expression, so it may be too complicated to auto-format into human readable text. For any conditionally-required input, the conditions upon which it is required should also be described in the `about` text.

## Limitations
- This implementation can only generate output that uses standard docutils features, and no sphinx-specific features. See natcap/invest.users-guide#35 for details.
- Documentation is generated for a key and everything below it. There is currently no way to generate only the first level, for example.
- Relies on the `ARGS_SPEC` being complete. For example, columns in a table's `columns` attribute should either all have an `about` attribute, or none have an `about` attribute. However, it is still valid for only some to have an `about` attribute. If some are missing, it will work, but the generated docs will look a little strange.

## Tests
From the top level of this repo, you can run `make test_investspec` to run a set of unit tests (`extensions/investspec/test/test_investspec.py`). These only test the formatting logic.

`make demo_investspec` exists as a sort-of integration test to prove that the extension works without errors. The output is not checked for correctness. It installs the mock module in `extensions/investspec/test/test_module`, then builds HTML docs from `extensions/investspec/test/index.rst`, using the `investspec` role. You can look at the output in `extensions/investspec/test/build` for examples of what the role does.
