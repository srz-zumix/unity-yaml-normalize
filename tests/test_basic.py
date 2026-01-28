"""Basic tests for unity-yaml-normalize"""
import unittest
import subprocess
import sys
from unityyamlnormalize import __version__


class TestBasic(unittest.TestCase):
    """Basic test cases"""

    def test_version(self):
        """Test that version is defined"""
        self.assertIsNotNone(__version__)
        self.assertIsInstance(__version__, str)


class TestInstallation(unittest.TestCase):
    """Installation test cases"""

    def test_module_import(self):
        """Test that the module can be imported"""
        import unityyamlnormalize
        self.assertIsNotNone(unityyamlnormalize)

    def test_submodules_import(self):
        """Test that submodules can be imported"""
        from unityyamlnormalize import __main__
        self.assertIsNotNone(__main__)

    def test_cli_command_exists(self):
        """Test that the CLI command is available"""
        result = subprocess.run(
            [sys.executable, '-m', 'unityyamlnormalize', '--version'],
            capture_output=True,
            text=True
        )
        # Check that the command runs (exit code 0)
        self.assertEqual(result.returncode, 0)
        # Check that version is in the output
        self.assertIn('version', result.stdout.lower() + result.stderr.lower())

    def test_cli_help(self):
        """Test that CLI help works"""
        result = subprocess.run(
            [sys.executable, '-m', 'unityyamlnormalize', '--help'],
            capture_output=True,
            text=True
        )
        self.assertEqual(result.returncode, 0)
        # Help should contain usage information
        self.assertIn('usage', result.stdout.lower())


if __name__ == '__main__':
    unittest.main()
