import unittest
import sys
import os

# Add the parent directory to the sys.path to access the introductory module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from introductory.increasing_array import calculate_moves

class TestIncreasingArray(unittest.TestCase):
    def test_increasing_array(self):
        self.assertEqual(calculate_moves([3, 2, 5, 1, 7]), 5)
        self.assertEqual(calculate_moves([6, 10, 4, 10, 2, 8, 9, 2, 7, 7]), 31)

if __name__ == '__main__':
    unittest.main()