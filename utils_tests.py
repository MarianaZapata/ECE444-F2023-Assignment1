import unittest
from utils import Utils  

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.utils = Utils()

    # Reversed Tests
    def test_reverse_integer(self):
        # Test integers
        self.assertEqual(self.utils.reversed(123), 321)

    def test_reverse_string(self):
        # Test strings (should raise ValueError)
        with self.assertRaises(ValueError):
            self.utils.reversed("123")

    def test_reverse_float(self):
        # Test floats (should raise ValueError)
        with self.assertRaises(ValueError):
            self.utils.reversed(1.1)

    # Formatter Tests
    def test_format_integer(self):
        # Test integers
        self.utils.formatter(42)

    def test_format_string(self):
        # Test strings (should raise ValueError)
        with self.assertRaises(ValueError):
            self.utils.formatter("42")

    def test_format_float(self):
        # Test floats (should raise ValueError)
        with self.assertRaises(ValueError):
            self.utils.formatter(12.34)

if __name__ == '__main__':
    unittest.main()
