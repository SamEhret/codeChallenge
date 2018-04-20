# To run tests:
# py.test treeClassTests.py

from unittest import TestCase
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
import treeClass

class TestNodeProperties(TestCase):
    # Test properties added correctly
    def test_properties_added_to_node_correct_place(self):
        value = 'value_string'
        newNode = treeClass.node(value)
        self.assertEqual(value, newNode.value)
    
    # Test that __str__ returns correct value
    def test_that_correct_string_is_retuned_for_node(self):
        root = treeClass.node('test')
        expectedString = 'test\n'
        self.assertEqual(expectedString, treeClass.node.__str__(root))

    # Test that __str__ returns correct with children
    def test_that_correct_string_returned_with_children(self):
        root = treeClass.node('')
        root.children = [treeClass.node('test')]
        root.children[0].children = [treeClass.node('child1'), treeClass.node('child2')]
        expectedString = '\ntest\n-child1\n-child2\n'
        self.assertEqual(expectedString, treeClass.node.__str__(root))