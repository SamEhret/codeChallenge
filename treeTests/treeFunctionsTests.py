# To run tests:
# py.test treeFunctionsTests.py

from unittest import TestCase
from unittest.mock import patch
import types
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


class TestIsValid(TestCase):
    # Test isValid = True
    def test_isValid_returns_true(self):
        validString = '(test)'
        self.assertTrue(treeFunctions.isValid(validString))

    # Test isValie = False
    def test_isValie_returns_false(self):
        invalidString = 'test'
        self.assertFalse(treeFunctions.isValid(invalidString))


class TestProcessInput(TestCase):
    # Test no ',' or '' in processed list
    def test_comma_and_empty_are_removed(self):
        testString = '(,apple,dog(t((, test)), k))'
        self.assertNotIn(',', treeFunctions.processInput(testString))
        self.assertNotIn('', treeFunctions.processInput(testString))
    

class TestProcessInputIsList(TestCase):
    # Test that list is list
    def test_processed_list_is_list(self):
        testString = '(test,,dot(call)happy(,bee,))'
        self.assertTrue(type(treeFunctions.processInput(testString)) is list, msg='Type is: ' + str(type(treeFunctions.processInput(testString))))


class TestBuildTreeReturnsObject(TestCase):
    # Test buildTree returns object
    def test_object_is_returned_from_buildTree(self):
        testString = '(test(bees, tree(happy),low,purple)'
        self.assertTrue(isinstance(treeFunctions.buildTree(testString), object))