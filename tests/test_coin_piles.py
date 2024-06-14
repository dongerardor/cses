import unittest
import sys
import os

# Add the parent directory to the sys.path to access the introductory module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from introductory.coin_piles import coin_piles

class TestCoinPiles(unittest.TestCase):
    def test_coin_piles(self):
        self.assertEqual(coin_piles([(2, 1), (2, 2), (3, 3)]), "YES\nNO\nYES\n")
        self.assertEqual(coin_piles([(1, 1), (1, 1), (1, 1)]), "NO\nNO\nNO\n")
        self.assertEqual(coin_piles([(1, 2), (1, 2), (1, 2)]), "YES\nYES\nYES\n")
        self.assertEqual(coin_piles([(1, 3), (1, 3), (1, 3)]), "NO\nNO\nNO\n")
        self.assertEqual(coin_piles([(1, 4), (1, 4), (1, 4)]), "NO\nNO\nNO\n")
        self.assertEqual(coin_piles([(1, 5), (1, 5), (1, 5)]), "NO\nNO\nNO\n")
        self.assertEqual(coin_piles([(1, 6), (1, 6), (1, 6)]), "NO\nNO\nNO\n")
        self.assertEqual(coin_piles([(1, 7), (1, 7), (1, 7)]), "NO\nNO\nNO\n")
        self.assertEqual(coin_piles([(1, 8), (1, 8), (1, 8)]), "NO\nNO\nNO\n")
        self.assertEqual(coin_piles([(1, 9), (1, 9), (1, 9)]), "NO\nNO\nNO\n")
        self.assertEqual(coin_piles([(1, 10), (1, 10), (1, 10)]), "NO\nNO\nNO\n")
        self.assertEqual(coin_piles([(1, 11), (1, 11), (1, 11)]), "NO\nNO\nNO\n")
        self.assertEqual(coin_piles([(1, 12), (1, 12), (1, 12)]), "NO\nNO\nNO\n")
        self.assertEqual(coin_piles([(1, 13), (1, 13), (1, 13)]), "NO\nNO\nNO\n")

if __name__ == '__main__':
    unittest.main()