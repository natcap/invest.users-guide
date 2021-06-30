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
        "workspace_dir": {
            "name": "Workspace",
            "about": (
                "The folder where all intermediate and output files of the model "
                "will be written.  If this folder does not exist, it will be "
                "created."),
            "type": "directory",
            "contents": {},
            "must_exist": False,
            "permissions": "rwx",
        },
        "results_suffix": {
            "name": "File suffix",
            "about": (
                'A string that will be added to the end of all files '
                'written to the workspace.'),
            "type": "freestyle_string",
            "required": False,
            "regexp": "[a-zA-Z0-9_-]*"
        },
        "n_workers": {
            "name": "Taskgraph n_workers parameter",
            "about": (
                "The n_workers parameter to provide to taskgraph. "
                "-1 will cause all jobs to run synchronously. "
                "0 will run all jobs in the same process, but scheduling will take "
                "place asynchronously. Any other positive integer will cause that "
                "many processes to be spawned to execute tasks."),
            "type": "number",
            "units": ureg.none,
            "required": False,
            "expression": "value >= -1"
        },
        "n_nearest_model_points": {
            "expression": "value > 0",
            "type": "number",
            "units": ureg.none,
            "required": "compute_forest_edge_effects",
            "about": (
                "Used when calculating the biomass in a pixel.  This number "
                "determines the number of closest regression models that are "
                "used when calculating the total biomass.  Each local model "
                "is linearly weighted by distance such that the biomass in "
                "the pixel is a function of each of these points with the "
                "closest point having the highest effect."),
            "name": "Number of nearest model points to average"
        },
        "aoi_vector_path": {
            "type": "vector",
            "fields": {},
            "geometries": {"POLYGON", "MULTIPOLYGON"},
            "name": "area of interest",
            "about": (
                "A polygon vector containing features over which to aggregate and "
                "summarize the final results."),
            "projected": True,
            "required": False
        },
        "biophysical_table_path": {
            "type": "csv",
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
                "c_below": {
                    "type": "number",
                    "units": ureg.metric_ton/ureg.hectare,
                    "required": "pools_to_calculate == 'all'",
                    "about": (
                        "Carbon density value for the belowground carbon pool")
                },
                "c_soil": {
                    "type": "number",
                    "units": ureg.metric_ton/ureg.hectare,
                    "required": "pools_to_calculate == 'all'",
                    "about": "Carbon density value for the soil carbon pool"
                },
                "c_dead": {
                    "type": "number",
                    "units": ureg.metric_ton/ureg.hectare,
                    "required": "pools_to_calculate == 'all'",
                    "about": (
                        "Carbon density value for the dead matter carbon pool")
                },
            },
            "about": (
                "A CSV table containing model information corresponding to "
                "each of the land use classes in the LULC raster input.  If "
                "the user selects 'all carbon pools' the table must also "
                "contain entries for 'c_below', 'c_soil', and 'c_dead'.  See "
                "the InVEST Forest Carbon User's Guide for more information "
                "about these fields."),
            "name": "Biophysical Table"
        },
        "lulc_raster_path": {
            "type": "raster",
            "bands": {1: {"type": "code"}},
            "about": "Map of land use/land cover codes.",
            "name": "land use/land cover",
            "projected": True
        },
        "pools_to_calculate": {
            "type": "option_string",
            "options": {
                "all": ("Use all pools (c_above, c_below, c_dead, and c_soil) "
                        "in the carbon pool calculation"),
                "above_ground": (
                    "Only use the c_above pool in the carbon pool calculation")
            },
            "about": "Which carbon pools to use (all or c_above only)",
            "name": "Carbon Pools to Calculate"
        },
        "compute_forest_edge_effects": {
            "type": "boolean",
            "about": (
                "If selected, will use the Chaplin-Kramer, et. al method to "
                "account for above ground carbon stocks in tropical forest "
                "types indicated by a '1' in the 'is_tropical_forest' field "
                "in the biophysical table."),
            "name": "Compute forest edge effects"
        },
        "tropical_forest_edge_carbon_model_vector_path": {
            "type": "vector",
            "fields": {
                "method": {
                    "type": "number",
                    "units": ureg.none,
                    "expression": "value in {1, 2, 3}"
                },
                "theta1": {"type": "number", "units": ureg.none},
                "theta2": {"type": "number", "units": ureg.none},
                "theta3": {"type": "number", "units": ureg.none}
            },
            "geometries": {"POLYGON", "MULTIPOLYGON"},
            "required": "compute_forest_edge_effects",
            "about": (
                "A vector with fields 'method', 'theta1', 'theta2', 'theta3' "
                "describing the global forest carbon edge models. Provided as "
                "default data for the model."),
            "name": "Global forest carbon edge regression models"
        },
        "biomass_to_carbon_conversion_factor": {
            "type": "ratio",
            "required": "compute_forest_edge_effects",
            "about": (
                "Number by which to scale forest edge biomass to convert to "
                "carbon.  Default value is 0.47 (according to IPCC 2006). "
                "This pertains to forest classes only; values in the "
                "biophysical table for non-forest classes should already be "
                "in terms of carbon, not biomass."),
            "name": "Forest Edge Biomass to Carbon Conversion Factor"
        }
    }
}
