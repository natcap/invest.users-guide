import pint

ureg = pint.UnitRegistry()
ureg.define('none = []')

ARGS_SPEC = {
    "model_name": "Forest Carbon Edge Effect Model",
    "module": __name__,
    "userguide_html": "carbon_edge.html",
    "args_with_spatial_overlap": {
        "spatial_keys": ["aoi_vector_path", "lulc_raster_path"],
    },
    "args": {
        "number_input": {
            "name": "Foo",
            "about": "Numbers have units that are displayed in a human-readable way.",
            "type": "number",
            "units": ureg.meter**3/ureg.month,
            "expression": "value >= 0"
        },
        "ratio_input": {
            "name": "Bar",
            "about": "Here's a ratio.",
            "type": "ratio"
        },
        "percent_input": {
            "name": "Baz",
            "about": "Here's a percent.",
            "type": "percent",
            "required": False
        },
        "code_input": {
            "name": "Abc",
            "about": "Here's a code.",
            "type": "code",
            "required": True
        },
        "boolean_input": {
            "name": "Defg",
            "about": "Here's a boolean.",
            "type": "boolean"
        },
        "freestyle_string_input": {
            "name": "Hijk",
            "about": (
                "Here's a freestyle string. If its spec has a `regexp` "
                "attribute, we don't display that. The `about` attribute "
                "should describe any required pattern in a user-friendly way."
            ),
            "type": "freestyle_string"
        },
        "option_string_input": {
            "name": "Lmn",
            "about": (
                "For option_strings, we display the options in a bullet list, "
                "sorted alphabetically."),
            "type": "option_string",
            "options": {
                "option_a": "do something",
                "option_b": "do something else"
            }
        },
        "raster_input": {
            "type": "raster",
            "bands": {1: {"type": "code"}},
            "about": "Rasters are pretty simple.",
            "name": "Opq"
        },
        "another_raster_input": {
            "type": "raster",
            "bands": {1: {
                "type": "number",
                "units": ureg.millimeter/ureg.year
            }},
            "about": (
                "If the raster's band is a `number` type, display its units"),
            "name": "Rst"
        },
        "basic_vector_input": {
            "type": "vector",
            "fields": {},
            "geometries": {"LINESTRING"},
            "about": "Display vector geometries in an ordered list.",
            "name": "Uvw"
        },
        "vector_input_with_fields": {
            "type": "vector",
            "fields": {
                "id": {
                    "type": "code",
                    "about": "Unique identifier for each feature"
                },
                "precipitation": {
                    "type": "number",
                    "units": ureg.millimeter/ureg.year,
                    "about": "Average annual precipitation over the area"
                }
            },
            "geometries": {"POLYGON", "MULTIPOLYGON"},
            "about": (
                "Vector fields are nested args that are documented "
                "recursively in an unordered bulleted list."),
            "name": "Xyz"
        },
        "basic_csv_input": {
            "type": "csv",
            "about": (
                "Unicode characters work too 😎 If a CSV's spec doesn't "
                "describe rows or columns, we add a note:"),
            "name": "☺"
        },
        "complicated_csv_input": {
            "type": "csv",
            "about": "CSVs are also recursive.",
            "name": "Foo",
            "columns": {
                "a": {
                    "type": "number",
                    "units": ureg.second,
                    "about": "Here's a description."
                },
                "b": {"type": "ratio", "about": "Here's a description."},
                "c": {"type": "percent", "about": "Here's a description."},
                "d": {"type": "code", "about": "Here's a description."},
                "e": {"type": "boolean", "about": "Here's a description."},
                "f": {"type": "freestyle_string", "about": "Here's a description."},
                "g": {
                    "type": "option_string",
                    "about": "Here's a description.",
                    "options": {
                        "1": "option 1",
                        "2": "option 2"
                    }
                },
                "h": {
                    "type": "raster",
                    "about": "Here's a description.",
                    "bands": {1: {"type": "number", "units": ureg.meter}}
                },
                "i": {
                    "type": "vector",
                    "about": "Here's a description.",
                    "geometries": {"POINT"},
                    "fields": {
                        "ws_id": {
                            "type": "code",
                            "about": "Unique watershed ID"
                        }
                    }
                },
                "j": {"type": "csv", "about": "Here's a description."},
                "k": {"type": "directory", "about": "Here's a description."},
                "l": {"type": "file", "about": "Here's a description."},
            }
        },
        "directory_input": {
            "type": "directory",
            "about": "Directories are recursive too.",
            "name": "Foo",
            "contents": {
                "foo": {
                    "type": "raster",
                    "bands": {1: {"type": "code"}}
                },
                "bar": {
                    "type": "vector",
                    "geometries": {"POLYGON"},
                    "fields": {
                        "ws_id": {
                            "type": "code",
                            "about": "Unique watershed ID"
                        }
                    }
                },
                "baz": {
                    "type": "csv",
                    "required": False,
                    "columns": {
                        "id": {"type": "code"},
                        "description": {
                            "type": "freestyle_string",
                            "required": False,
                            "about": "a description of the id"
                        },
                        "raster_path": {
                            "type": "raster",
                            "bands": {1: {"type": "number", "units": ureg.meter}}
                        }
                    }
                },
                "abc": {"type": "directory"},
                "xyz": {"type": "file"}
            }
        }
    }
}
