# To run tests:
# py.test treeClassTests.py

from unittest import TestCase
from unittest.mock import patch
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import treeClass

class TestNodeProperties(TestCase):
    # Check properties added correctly
    def test_properties_added_to_node_correct_place(self):
        # Arrange
        value = 'value_string'
        parent = None
        children = []

        # Act
        newNode = treeClass.node(value, parent, children)

        # Assert
        self.assertEqual(value, newNode.value)
        self.assertEqual(parent, newNode.parent)
        self.assertEqual(children, newNode.children)