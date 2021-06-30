# investspec extension for Sphinx

This is a custom Sphinx extension that generates documentation of InVEST model inputs from the model's `ARGS_SPEC`.
Its purpose is to help us reduce duplicated information and provide consistent, user-friendly documentation.
The `investspec` extension provides the `:investspec:` role, which can be used inline in RST files to insert generated documentation anywhere you want.

## setup

`investspec` is already set up in the `conf.py` in this repo.

In case we need to use it anywhere else, here's how to set it up:
In the `conf.py` file for the source RST, add the `investspec/` root directory to `sys.path` so that Sphinx can find it:
```
sys.path.append(os.path.abspath('../extensions/investspec'))
```
and add `investspec` to the list of extensions:
```
extensions = ['investspec']
```

## usage


## tests
Testing this