# To run tests:
# py.test treeClassTests.py

from unittest import TestCase
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
import treeClass

class TestNodeProperties(TestCase):
    # Check properties added correctly
    def test_properties_added_to_node_correct_place(self):
        # Arrange
        value = 'value_string'

        # Act
        newNode = treeClass.node(value)

        # Assert
        self.assertEqual(value, newNode.value)