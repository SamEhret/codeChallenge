# To run tests:
# py.test treeFunctionsTests.py

from unittest import TestCase
from unittest.mock import patch
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import treeFunctions

class TestInputIsString(TestCase):
    # Test manual input is string
    @patch('builtins.input', lambda x: 'test')
    def test_input_is_string(self):
        self.assertTrue(type(treeFunctions.getInput()) is str, msg='Type is: ' + str(type(treeFunctions.getInput())))
    
    # Test numeric input is string
    @patch('builtins.input', lambda x: '123')
    def test_numeric_input_is_string(self):
        self.assertTrue(type(treeFunctions.getInput()) is str, msg='Type is: ' + str(type(treeFunctions.getInput())))
    
    # Test default is string
    @patch('builtins.input', lambda x: '')
    def test_default_input_is_string(self):
        self.assertTrue(type(treeFunctions.getInput()) is str, msg='Type is: ' + str(type(treeFunctions.getInput())))


class TestInputMatchesString(TestCase):
    # Test default input matches hard-coded default
    @patch('builtins.input', lambda x: '')
    def test_default_matches_default(self):
        default = '(id,created,employee(id,firstname,employeeType(id),lastname),location)'
        self.assertEqual(default, treeFunctions.getInput())
    
    # Test string matches manual input
    @patch('builtins.input', lambda x: 'test_string')
    def test_manual_input_matches_string(self):
        self.assertEqual('test_string', treeFunctions.getInput())