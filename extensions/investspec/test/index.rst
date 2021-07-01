
Here are examples of how each arg type gets displayed.
You can pass the module name as the only argument to the investspec role, and it will document every arg in the spec:

:investspec:`test_module`

You can pass a second argument to the role, that says which arg or arg property to document.
Here is a directory, that contains a CSV, that contains a column of raster paths:

:investspec:`test_module directory_input`

You can access any attribute or nested arg by a period-separated series of keys. Here is just the list of directory contents:

:investspec:`test_module directory_input.contents`

Here is just the nested CSV:

:investspec:`test_module directory_input.contents.baz`

Here is the list of the nested CSV's columns:

:investspec:`test_module directory_input.contents.baz.columns`

Here is the raster column:

:investspec:`test_module directory_input.contents.baz.columns.raster_path`

Here is the raster units:

:investspec:`test_module directory_input.contents.baz.columns.raster_path.bands.1.units`

You can use them in-line too: :investspec:`test_module directory_input.name` is the name of this arg.


.. toctree::
    input_types
