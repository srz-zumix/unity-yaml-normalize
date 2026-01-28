"""Basic tests for unity-yaml-normalize"""
import unittest
from unityyamlnormalize import __version__


class TestBasic(unittest.TestCase):
    """Basic test cases"""

    def test_version(self):
        """Test that version is defined"""
        self.assertIsNotNone(__version__)
        self.assertIsInstance(__version__, str)


if __name__ == '__main__':
    unittest.main()
