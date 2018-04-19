# To run tests:
# py.test inputFunctionsTests.py

from unittest import TestCase
from unittest.mock import patch
import types
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
import inputFunctions

class TestInputIsString(TestCase):
    # Test manual input is string
    @patch('builtins.input', lambda x: 'test')
    def test_input_is_string(self):
        self.assertTrue(type(inputFunctions.getInput()) is str, msg='Type is: ' + str(type(inputFunctions.getInput())))
    
    # Test numeric input is string
    @patch('builtins.input', lambda x: '123')
    def test_numeric_input_is_string(self):
        self.assertTrue(type(inputFunctions.getInput()) is str, msg='Type is: ' + str(type(inputFunctions.getInput())))
    
    # Test default is string
    @patch('builtins.input', lambda x: '')
    def test_default_input_is_string(self):
        self.assertTrue(type(inputFunctions.getInput()) is str, msg='Type is: ' + str(type(inputFunctions.getInput())))


class TestInputMatchesString(TestCase):
    # Test default input matches hard-coded default
    @patch('builtins.input', lambda x: '')
    def test_default_matches_default(self):
        default = '(id,created,employee(id,firstname,employeeType(id),lastname),location)'
        self.assertEqual(default, inputFunctions.getInput())
    
    # Test string matches manual input
    @patch('builtins.input', lambda x: 'test_string')
    def test_manual_input_matches_string(self):
        self.assertEqual('test_string', inputFunctions.getInput())


class TestIsValid(TestCase):
    # Test isValid = True
    def test_isValid_returns_true(self):
        validString = '(test)'
        self.assertTrue(inputFunctions.isValid(validString))

    # Test isValie = False
    def test_isValid_returns_false(self):
        invalidString = 'test'
        self.assertFalse(inputFunctions.isValid(invalidString))


class TestProcessInput(TestCase):
    # Test no ',' or '' in processed list
    def test_comma_and_empty_are_removed(self):
        testString = '(,apple,dog(t((, test)), k))'
        self.assertNotIn(',', inputFunctions.processInput(testString))
        self.assertNotIn('', inputFunctions.processInput(testString))
    

class TestProcessInputIsList(TestCase):
    # Test that list is list
    def test_processed_list_is_list(self):
        testString = '(test,,dot(call)happy(,bee,))'
        self.assertTrue(type(inputFunctions.processInput(testString)) is filter, msg='Type is: ' + str(type(inputFunctions.processInput(testString))))