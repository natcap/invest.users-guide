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

The `investspec` role takes two arguments: `` :investspec:`module key` ``

`module` (or `f'{investspec_module_prefix}.{module}'` if `investspec_module_prefix` is defined) must be an importable python module. It must have an attribute `ARGS_SPEC` that is a well-formed InVEST args spec dictionary.

The second argument specifies which (nested) arg to document. It is a period-separated series of dictionary keys accessed starting at `ARGS_SPEC.args`. For example:
```
ARGS_SPEC = {
    "model_name": "InVEST Model",
    "args": {
        "biophysical_table_path": {
            "type": "csv",
            "name": "Biophysical Table"
            "columns": {
                "lucode": {"type": "integer"},
                "path": {
                    "type": "vector",
                    "fields": {
                        "value": {
                            "type": "integer"
                        }
                    }
                }
            }

...
}
```
If this model is located at `natcap.invest.model_name`, then you can auto-document:

- `` :investspec:`model_name biophysical_table_path` ``

- `` :investspec:`model_name biophysical_table_path.columns.path` ``

- `` :investspec:`model_name biophysical_table_path.columns.path.fields.value` ``

You can document any arg in the `ARGS_SPEC.args` dictionary this way. This includes any nested dictionary with a `type` attribute:

- top-level args
- any row or column within a csv's `"rows"` or `"columns"` dict
- any field within a vector's `"fields"` dict
- any file or directory within a directory's `"contents"` dict

## What is not documented
- `expression`s for `number` types. This can be any python expression, so it may be too complicated to to auto-format into human readable text. Any limits on a `number`'s value should also be described in the `about` text.
- Conditional requirements (`"required": <str>`). This can be any python expression, so it may be too complicated to auto-format into human readable text. For any conditionally-required input, the conditions upon which it is required should also be described in the `about` text.

## Limitations
- This implementation can only generate output that uses standard docutils features, and no sphinx-specific features. See natcap/invest.users-guide#35 for details.
- Relies on the `ARGS_SPEC` being complete. For example, columns in a table's `columns` attribute should either all have an `about` attribute, or none have an `about` attribute. However, it is still valid for only some to have an `about` attribute. If some are missing, it will work, but the generated docs will look a little strange.

## Tests
From the top level of this repo, you can run `make test_investspec` to run a set of unit tests (`extensions/investspec/test/test_investspec.py`). These only test the formatting logic.

`make demo_investspec` exists as a sort-of integration test to prove that the extension works without errors. The output is not checked for correctness. It installs the mock module in `extensions/investspec/test/test_module`, then builds HTML docs from `extensions/investspec/test/index.rst`, using the `investspec` role. You can look at the output in `extensions/investspec/test/build` for examples of what the role does.
