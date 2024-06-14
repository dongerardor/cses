import unittest
import sys
import os

# Add the parent directory to the sys.path to access the introductory module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from introductory.bit_strings import binary_string

class TestBitString(unittest.TestCase):
    def test_bit_string(self):
        self.assertEqual(binary_string(0), 1)
        self.assertEqual(binary_string(1), 2)
        self.assertEqual(binary_string(2), 4)
        self.assertEqual(binary_string(3), 8)
        self.assertEqual(binary_string(4), 16)
        self.assertEqual(binary_string(27), 134217728)
        self.assertEqual(binary_string(255), 396422633)
        self.assertEqual(binary_string(159487), 291864888)

if __name__ == '__main__':
    unittest.main()