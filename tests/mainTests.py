# To run tests:
# py.test mainTests.py

from unittest import TestCase
from unittest.mock import patch
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

class TestIsValidContinuesOrEnds(TestCase):
    # Test isValid ends when False
    @patch('builtins.input', lambda x: 'invalid')
    def test_inValid_is_false_system_exit(self):
        with self.assertRaises(SystemExit):
            import main