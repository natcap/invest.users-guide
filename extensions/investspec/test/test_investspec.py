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

    # def test_number_spec(self):
    #     spec = {
    #         "name": "Bar",
    #         "about": "Description",
    #         "type": "number",
    #         "units": ureg.meter**3/ureg.month,
    #         "expression": "value >= 0"
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = (
    #         '**Bar** (:ref:`number <number>`, meter ** 3 / month, required): Description\n\n'
    #         'Constraints: value >= 0'
    #     )
    #     self.assertEqual(out, expected_rst)

    # def test_ratio_spec(self):
    #     spec = {
    #         "name": "Bar",
    #         "about": "Description",
    #         "type": "ratio"
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = '**Bar** (:ref:`ratio <ratio>`, required): Description'
    #     self.assertEqual(out, expected_rst)

    # def test_percent_spec(self):
    #     spec = {
    #         "name": "Bar",
    #         "about": "Description",
    #         "type": "percent",
    #         "required": False
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = '**Bar** (:ref:`percent <percent>`, optional): Description'
    #     self.assertEqual(out, expected_rst)

    # def test_code_spec(self):
    #     spec = {
    #         "name": "Bar",
    #         "about": "Description",
    #         "type": "code",
    #         "required": True
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = '**Bar** (:ref:`code <code>`, required): Description'
    #     self.assertEqual(out, expected_rst)

    # def test_boolean_spec(self):
    #     spec = {
    #         "name": "Bar",
    #         "about": "Description",
    #         "type": "boolean"
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = '**Bar** (:ref:`true/false <truefalse>`, required): Description'
    #     self.assertEqual(out, expected_rst)

    # def test_freestyle_string_spec(self):
    #     spec = {
    #         "name": "Bar",
    #         "about": "Description",
    #         "type": "freestyle_string"
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = '**Bar** (:ref:`text <text>`, required): Description'
    #     self.assertEqual(out, expected_rst)

    # def test_option_string_spec(self):
    #     spec = {
    #         "name": "Bar",
    #         "about": "Description",
    #         "type": "option_string",
    #         "options": {
    #             "option_a": "do something",
    #             "option_b": "do something else"
    #         }
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = (
    #         '**Bar** (:ref:`option <option>`, required): Description\n'
    #         'Options:\n\n'
    #         '- option_a: do something\n\n'
    #         '- option_b: do something else'
    #     )
    #     self.assertEqual(out, expected_rst)

    # def test_raster_spec(self):
    #     spec = {
    #         "type": "raster",
    #         "bands": {1: {"type": "code"}},
    #         "about": "Description",
    #         "name": "Bar"
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = (
    #         '**Bar** (:ref:`raster <raster>`, required): Description'
    #     )
    #     self.assertEqual(out, expected_rst)

    #     spec = {
    #         "type": "raster",
    #         "bands": {1: {
    #             "type": "number",
    #             "units": ureg.millimeter/ureg.year
    #         }},
    #         "about": "Description",
    #         "name": "Bar"
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = (
    #         '**Bar** (:ref:`raster <raster>`, required): Description\n\n'
    #         'units: millimeter / year')
    #     self.assertEqual(out, expected_rst)

    # def test_vector_spec(self):
    #     spec = {
    #         "type": "vector",
    #         "fields": {},
    #         "geometries": {"LINESTRING"},
    #         "about": "Description",
    #         "name": "Bar"
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = (
    #         '**Bar** (:ref:`vector <vector>`, required): Description\n'
    #         'Geometries: linestring'
    #     )
    #     self.assertEqual(out, expected_rst)

    #     spec = {
    #         "type": "vector",
    #         "fields": {
    #             "id": {
    #                 "type": "code",
    #                 "about": "Unique identifier for each feature"
    #             },
    #             "precipitation": {
    #                 "type": "number",
    #                 "units": ureg.millimeter/ureg.year,
    #                 "about": "Average annual precipitation over the area"
    #             }
    #         },
    #         "geometries": {"POLYGON", "MULTIPOLYGON"},
    #         "about": "Description",
    #         "name": "Bar"
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = (
    #         '**Bar** (:ref:`vector <vector>`, required): Description\n'
    #         'Geometries: polygon, multipolygon\n'
    #         'Fields:\n'
    #         '- **id** (:ref:`code <code>`, required): Unique identifier for each feature\n'
    #         '- **precipitation** (:ref:`number <number>`, millimeters/year, required): Average annual precipitation over the area'
    #     )
    #     self.assertEqual(out, expected_rst)

    # def test_csv_spec(self):
    #     spec = {
    #         "type": "csv",
    #         "about": "Description",
    #         "name": "Bar"
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = (
    #         '**Bar** (:ref:`csv <csv>`, required): Description\n'
    #         'Please see the sample data table for details on the format.'
    #     )
    #     self.assertEqual(out, expected_rst)

    #     # Test every type that can be nested in a CSV column:
    #     # number, ratio, percent, code,
    #     spec = {
    #         "type": "csv",
    #         "about": "Description",
    #         "name": "Bar",
    #         "columns": {
    #             "a": {
    #                 "type": "number",
    #                 "units": ureg.second,
    #                 "about": "description"
    #             },
    #             "b": {"type": "ratio", "about": "description"},
    #             "c": {"type": "percent", "about": "description"},
    #             "d": {"type": "code", "about": "description"},
    #             "e": {"type": "boolean", "about": "description"},
    #             "f": {"type": "freestyle_string", "about": "description"},
    #             "g": {
    #                 "type": "option_string",
    #                 "about": "description",
    #                 "options": {
    #                     "1": "option 1",
    #                     "2": "option 2"
    #                 }
    #             },
    #             "h": {
    #                 "type": "raster",
    #                 "about": "description",
    #                 "bands": {1: {"type": "number", "units": ureg.meter}}
    #             },
    #             "i": {
    #                 "type": "vector",
    #                 "about": "description",
    #                 "geometries": {"POINT"},
    #                 "fields": {
    #                     "ws_id": {
    #                         "type": "code",
    #                         "about": "Unique watershed ID"
    #                     }
    #                 }
    #             },
    #             "j": {"type": "csv", "about": "description"},
    #             "k": {"type": "directory", "about": "description"},
    #             "l": {"type": "file", "about": "description"},
    #         }
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = (
    #         '**Bar** (:ref:`csv <csv>`, required): Description\n'
    #         'Columns:\n'
    #         '- a (number, seconds, required): description\n'
    #         '- b (ratio, required): description\n'
    #         '- c (percent, required): description\n'
    #         '- d (code, required): description\n'
    #         '- e (true/false, required): description\n'
    #         '- f (text, required): description\n'
    #         '- g (option, required): description\n'
    #         '    Options:\n'
    #         '    - 1: option 1\n'
    #         '    - 2: option 2\n'
    #         '- h (raster, required): description\n'
    #         '    Units: meters\n'
    #         '- i (vector, required): description\n'
    #         '    Geometries: point\n'
    #         '    Fields:\n'
    #         '    - ws_id (code, required): Unique watershed ID'
    #         '- j (csv, required): description\n'
    #         '    Please see the sample data table for details on the format.\n'
    #         '- k (directory, required): description\n'
    #         '- l (file, required): description\n'
    #     )
    #     self.assertEqual(out, expected_rst)

    # def test_directory_spec(self):
    #     self.maxDiff = None
    #     spec = {
    #         "type": "directory",
    #         "about": "Description",
    #         "name": "Bar",
    #         "contents": {
    #             "foo": {
    #                 "type": "raster",
    #                 "bands": {1: {"type": "code"}}
    #             },
    #             "bar": {
    #                 "type": "vector",
    #                 "geometries": {"POLYGON"},
    #                 "fields": {
    #                     "ws_id": {
    #                         "type": "code",
    #                         "about": "Unique watershed ID"
    #                     }
    #                 }
    #             },
    #             "baz": {
    #                 "type": "csv",
    #                 "required": False,
    #                 "rows": {
    #                     "id": {"type": "code"},
    #                     "description": {
    #                         "type": "freestyle_string",
    #                         "required": False,
    #                         "about": "a description of the id"
    #                     }
    #                 }
    #             },
    #             "abc": {"type": "directory"},
    #             "xyz": {"type": "file"}
    #         }
    #     }
    #     out = investspec.format_spec(spec['name'], spec)
    #     expected_rst = (
    #         '**Bar** (`directory <directory>`, required): Description\n\n'
    #         'Contents:\n\n'
    #         '- **foo** (:ref:`raster <raster>`, required)\n\n'
    #         '- **bar** (:ref:`vector <vector>`, required)\n\n'
    #         '  Geometries: polygon\n\n'
    #         '  Fields:\n\n'
    #         '  - **ws_id** (:ref:`code <code>`, required): Unique watershed ID\n\n'
    #         '- **baz** (:ref:`csv <csv>`, optional)\n\n'
    #         '  Rows:\n\n'
    #         '  - **id** (:ref:`code <code>`, required)\n\n'
    #         '  - **description** (:ref:`text <text>`, optional): a description of the id\n\n'
    #         '- **abc** (:ref:`directory <directory>`, required)\n\n'
    #         '- **xyz** (:ref:`file <file>`, required)'
    #     )
    #     self.assertEqual(out, expected_rst)

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
