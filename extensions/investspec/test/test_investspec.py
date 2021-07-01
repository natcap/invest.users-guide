import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

import pint
from docutils.core import publish_from_doctree

import investspec

ureg = pint.UnitRegistry()
ureg.define('none = []')


class TestInvestSpec(unittest.TestCase):

    def test_number_spec(self):
        spec = {
            "name": "Bar",
            "about": "Description",
            "type": "number",
            "units": ureg.meter**3/ureg.month,
            "expression": "value >= 0"
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = (
            '**Bar** (`number <input_types.html#number>`__, '
            'meters^3/month, required): Description')
        self.assertEqual(repr(out), repr(expected_rst))

    def test_ratio_spec(self):
        spec = {
            "name": "Bar",
            "about": "Description",
            "type": "ratio"
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = ('**Bar** (`ratio <input_types.html#ratio>`__, '
                        'required): Description')
        self.assertEqual(repr(out), repr(expected_rst))

    def test_percent_spec(self):
        spec = {
            "name": "Bar",
            "about": "Description",
            "type": "percent",
            "required": False
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = ('**Bar** (`percent <input_types.html#percent>`__, '
                        'optional): Description')
        self.assertEqual(repr(out), repr(expected_rst))

    def test_code_spec(self):
        spec = {
            "name": "Bar",
            "about": "Description",
            "type": "code",
            "required": True
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = ('**Bar** (`code <input_types.html#code>`__, '
                        'required): Description')
        self.assertEqual(repr(out), repr(expected_rst))

    def test_boolean_spec(self):
        spec = {
            "name": "Bar",
            "about": "Description",
            "type": "boolean"
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = ('**Bar** (`true/false <input_types.html#truefalse>'
                        '`__, required): Description')
        self.assertEqual(repr(out), repr(expected_rst))

    def test_freestyle_string_spec(self):
        spec = {
            "name": "Bar",
            "about": "Description",
            "type": "freestyle_string"
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = ('**Bar** (`text <input_types.html#text>`__, '
                        'required): Description')
        self.assertEqual(repr(out), repr(expected_rst))

    def test_option_string_spec_dictionary(self):
        spec = {
            "name": "Bar",
            "about": "Description",
            "type": "option_string",
            "options": {
                "option_a": "do something",
                "option_b": "do something else"
            }
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = (
            '**Bar** (`option <input_types.html#option>`__, required): Description\n\n'
            '\tOptions:\n\n'
            '\t- option_a: do something\n\n'
            '\t- option_b: do something else'
        )
        self.assertEqual(repr(out), repr(expected_rst))

    def test_option_string_spec_set(self):
        spec = {
            "name": "Bar",
            "about": "Description",
            "type": "option_string",
            "options": {"option_a", "option_b"}
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = (
            '**Bar** (`option <input_types.html#option>`__, required): Description\n\n'
            '\tOptions: option_a, option_b'
        )
        self.assertEqual(repr(out), repr(expected_rst))

    def test_raster_spec(self):
        spec = {
            "type": "raster",
            "bands": {1: {"type": "code"}},
            "about": "Description",
            "name": "Bar"
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = (
            '**Bar** (`raster <input_types.html#raster>`__, required): Description'
        )
        self.assertEqual(repr(out), repr(expected_rst))

        spec = {
            "type": "raster",
            "bands": {1: {
                "type": "number",
                "units": ureg.millimeter/ureg.year
            }},
            "about": "Description",
            "name": "Bar"
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = '**Bar** (`raster <input_types.html#raster>`__, millimeters/year, required): Description'
        self.assertEqual(repr(out), repr(expected_rst))

    def test_vector_spec(self):
        spec = {
            "type": "vector",
            "fields": {},
            "geometries": {"LINESTRING"},
            "about": "Description",
            "name": "Bar"
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = (
            '**Bar** (`vector <input_types.html#vector>`__, required): Description\n\n'
            '\tAccepted geometries: linestring'
        )
        self.assertEqual(repr(out), repr(expected_rst))

        spec = {
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
            "about": "Description",
            "name": "Bar"
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = (
            '**Bar** (`vector <input_types.html#vector>`__, required): Description\n\n'
            '\tAccepted geometries: polygon, multipolygon\n\n'
            '\tFields:\n\n'
            '\t- \t**id** (`code <input_types.html#code>`__, required): Unique identifier for each feature\n\n'
            '\t- \t**precipitation** (`number <input_types.html#number>`__, millimeters/year, required): Average annual precipitation over the area'
        )
        self.assertEqual(repr(out), repr(expected_rst))

    def test_csv_spec(self):
        spec = {
            "type": "csv",
            "about": "Description.",
            "name": "Bar"
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = (
            '**Bar** (`csv <input_types.html#csv>`__, required): Description. '
            'Please see the sample data table for details on the format.'
        )
        self.assertEqual(repr(out), repr(expected_rst))

        # Test every type that can be nested in a CSV column:
        # number, ratio, percent, code,
        spec = {
            "type": "csv",
            "about": "Description",
            "name": "Bar",
            "columns": {
                "a": {
                    "type": "number",
                    "units": ureg.second,
                    "about": "description"
                },
                "b": {"type": "ratio", "about": "description"},
                "c": {"type": "percent", "about": "description"},
                "d": {"type": "code", "about": "description"},
                "e": {"type": "boolean", "about": "description"},
                "f": {"type": "freestyle_string", "about": "description"},
                "g": {
                    "type": "option_string",
                    "about": "description",
                    "options": {
                        "1": "option 1",
                        "2": "option 2"
                    }
                },
                "h": {
                    "type": "raster",
                    "about": "description",
                    "bands": {1: {"type": "number", "units": ureg.meter}}
                },
                "i": {
                    "type": "vector",
                    "about": "description",
                    "geometries": {"POINT"},
                    "fields": {
                        "ws_id": {
                            "type": "code",
                            "about": "Unique watershed ID"
                        }
                    }
                },
                "j": {"type": "csv", "about": "description"},
                "k": {"type": "directory", "about": "description"},
                "l": {"type": "file", "about": "description"},
            }
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = (
            '**Bar** (`csv <input_types.html#csv>`__, required): Description\n\n'
            '\tColumns:\n\n'
            '\t- \t**a** (`number <input_types.html#number>`__, seconds, required): description\n\n'
            '\t- \t**b** (`ratio <input_types.html#ratio>`__, required): description\n\n'
            '\t- \t**c** (`percent <input_types.html#percent>`__, required): description\n\n'
            '\t- \t**d** (`code <input_types.html#code>`__, required): description\n\n'
            '\t- \t**e** (`true/false <input_types.html#truefalse>`__, required): description\n\n'
            '\t- \t**f** (`text <input_types.html#text>`__, required): description\n\n'
            '\t- \t**g** (`option <input_types.html#option>`__, required): description\n\n'
            '\t\tOptions:\n\n'
            '\t\t- 1: option 1\n\n'
            '\t\t- 2: option 2\n\n'
            '\t- \t**h** (`raster <input_types.html#raster>`__, meters, required): description\n\n'
            '\t- \t**i** (`vector <input_types.html#vector>`__, required): description\n\n'
            '\t\tAccepted geometries: point\n\n'
            '\t\tFields:\n\n'
            '\t\t- \t\t**ws_id** (`code <input_types.html#code>`__, required): Unique watershed ID\n\n'
            '\t- \t**j** (`csv <input_types.html#csv>`__, required): description '
            'Please see the sample data table for details on the format.\n\n'
            '\t- \t**k** (`directory <input_types.html#directory>`__, required): description\n\n'
            '\t- \t**l** (`file <input_types.html#file>`__, required): description'
        )
        self.assertEqual(repr(out), repr(expected_rst))

    def test_directory_spec(self):
        self.maxDiff = None
        spec = {
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
                    "rows": {
                        "id": {"type": "code"},
                        "description": {
                            "type": "freestyle_string",
                            "required": False,
                            "about": "a description of the id"
                        }
                    }
                },
                "abc": {"type": "directory"},
                "xyz": {"type": "file"}
            }
        }
        out = investspec.format_arg(spec['name'], spec, indent='')
        expected_rst = (
            '**Bar** (`directory <input_types.html#directory>`__, required): Description\n\n'
            '\tContents:\n\n'
            '\t- \t**foo** (`raster <input_types.html#raster>`__, required)\n\n'
            '\t- \t**bar** (`vector <input_types.html#vector>`__, required)\n\n'
            '\t\tAccepted geometries: polygon\n\n'
            '\t\tFields:\n\n'
            '\t\t- \t\t**ws_id** (`code <input_types.html#code>`__, required): Unique watershed ID\n\n'
            '\t- \t**baz** (`csv <input_types.html#csv>`__, optional)\n\n'
            '\t\tRows:\n\n'
            '\t\t- \t\t**id** (`code <input_types.html#code>`__, required)\n\n'
            '\t\t- \t\t**description** (`text <input_types.html#text>`__, optional): a description of the id\n\n'
            '\t- \t**abc** (`directory <input_types.html#directory>`__, required)\n\n'
            '\t- \t**xyz** (`file <input_types.html#file>`__, required)'
        )
        self.assertEqual(repr(out), repr(expected_rst))

    def test_full_rst_file(selrf):

        test_dir = os.path.join(os.getcwd(), 'test')

        workspace_dir = tempfile.mkdtemp()
        subprocess.run(['pip', 'install', test_dir])
        subprocess.run(['pip', 'list'])
        subprocess.run(
            ['sphinx-build', '-W', '-b', 'html', './test/', workspace_dir]
        )


if __name__ == '__main__':
    unittest.main()
