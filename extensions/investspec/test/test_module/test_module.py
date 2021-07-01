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
            "about": "Lorem ipsum dolor sit amet.",
            "type": "number",
            "units": ureg.meter**3/ureg.month,
            "expression": "value >= 0"
        },
        "ratio_input": {
            "name": "Bar",
            "about": "Lorem ipsum dolor sit amet.",
            "type": "ratio"
        },
        "percent_input": {
            "name": "Baz",
            "about": "Lorem ipsum dolor sit amet.",
            "type": "percent",
            "required": False
        },
        "code_input": {
            "name": "Abc",
            "about": "Lorem ipsum dolor sit amet.",
            "type": "code",
            "required": True
        },
        "boolean_input": {
            "name": "Defg",
            "about": "Lorem ipsum dolor sit amet.",
            "type": "boolean"
        },
        "freestyle_string_input": {
            "name": "Hijk",
            "about": "Lorem ipsum dolor sit amet.",
            "type": "freestyle_string"
        },
        "option_string_input": {
            "name": "Lmn",
            "about": "Lorem ipsum dolor sit amet.",
            "type": "option_string",
            "options": {
                "option_a": "do something",
                "option_b": "do something else"
            }
        },
        "raster_input": {
            "type": "raster",
            "bands": {1: {"type": "code"}},
            "about": "Lorem ipsum dolor sit amet.",
            "name": "Opq"
        },
        "another_raster_input": {
            "type": "raster",
            "bands": {1: {
                "type": "number",
                "units": ureg.millimeter/ureg.year
            }},
            "about": "Lorem ipsum dolor sit amet.",
            "name": "Rst"
        },
        "basic_vector_input": {
            "type": "vector",
            "fields": {},
            "geometries": {"LINESTRING"},
            "about": "Lorem ipsum dolor sit amet.",
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
            "about": "Lorem ipsum dolor sit amet.",
            "name": "Xyz"
        },
        "basic_csv_input": {
            "type": "csv",
            "about": "Lorem ipsum dolor sit amet.",
            "name": "☺"
        },
        "complicated_csv_input": {
            "type": "csv",
            "about": "Lorem ipsum dolor sit amet.",
            "name": "Foo",
            "columns": {
                "a": {
                    "type": "number",
                    "units": ureg.second,
                    "about": "Lorem ipsum dolor sit amet."
                },
                "b": {"type": "ratio", "about": "Lorem ipsum dolor sit amet."},
                "c": {"type": "percent", "about": "Lorem ipsum dolor sit amet."},
                "d": {"type": "code", "about": "Lorem ipsum dolor sit amet."},
                "e": {"type": "boolean", "about": "Lorem ipsum dolor sit amet."},
                "f": {"type": "freestyle_string", "about": "Lorem ipsum dolor sit amet."},
                "g": {
                    "type": "option_string",
                    "about": "Lorem ipsum dolor sit amet.",
                    "options": {
                        "1": "option 1",
                        "2": "option 2"
                    }
                },
                "h": {
                    "type": "raster",
                    "about": "Lorem ipsum dolor sit amet.",
                    "bands": {1: {"type": "number", "units": ureg.meter}}
                },
                "i": {
                    "type": "vector",
                    "about": "Lorem ipsum dolor sit amet.",
                    "geometries": {"POINT"},
                    "fields": {
                        "ws_id": {
                            "type": "code",
                            "about": "Unique watershed ID"
                        }
                    }
                },
                "j": {"type": "csv", "about": "Lorem ipsum dolor sit amet."},
                "k": {"type": "directory", "about": "Lorem ipsum dolor sit amet."},
                "l": {"type": "file", "about": "Lorem ipsum dolor sit amet."},
            }
        },
        "directory_input": {
            "type": "directory",
            "about": "Description",
            "name": "Bar",
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
