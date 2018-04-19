# To run tests:
# py.test treeFunctionsTests.py

from unittest import TestCase
from unittest.mock import patch
import types
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
import treeFunctions

class TestBuildTreeReturnsObject(TestCase):
    # Test buildTree returns object
    def test_object_is_returned_from_buildTree(self):
        testString = '(test(bees, tree(happy),low,purple)'
        self.assertTrue(isinstance(treeFunctions.buildTree(testString), object))