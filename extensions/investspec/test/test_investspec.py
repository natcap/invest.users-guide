import unittest
from unittest.mock import MagicMock

import investspec
from docutils.nodes import emphasis, Node, reference, strong


class TestInvestSpec(unittest.TestCase):

    def test_parse_rst(self):
        """parse_rst should create a correct list of docutils nodes."""
        nodes = investspec.parse_rst(
            '**Bar** (`number <input_types.html#number>`__, '
            'units: **m³/month**, *required*): Description')
        self.assertEqual(type(nodes[0]), strong)
        self.assertEqual(nodes[0].children[0], 'Bar')
        self.assertEqual(nodes[1], ' (')
        self.assertEqual(type(nodes[2]), reference)
        self.assertEqual(nodes[2].children[0], 'number')
        self.assertEqual(nodes[3], ', units: ')
        self.assertEqual(type(nodes[4]), strong)
        self.assertEqual(nodes[4].children[0], 'm³/month')
        self.assertEqual(nodes[5], ', ')
        self.assertEqual(type(nodes[6]), emphasis)
        self.assertEqual(nodes[6].children[0], 'required')
        self.assertEqual(nodes[7], '): Description')

    def test_invest_spec(self):
        """invest_spec role function should return what sphinx expects."""
        mock_inliner = MagicMock()
        mock_inliner.document.settings.env.app.config.investspec_module_prefix = 'test_module'
        mock_inliner.document.settings.env.app.config.language = 'en'
        nodes, messages = investspec.invest_spec(
            None, None, 'test_module number_input', None, mock_inliner)
        print(nodes)
        self.assertEqual(len(nodes), 8)
        for node in nodes:
            self.assertTrue(isinstance(node, Node))
        self.assertEqual(messages, [])


if __name__ == '__main__':
    unittest.main()

