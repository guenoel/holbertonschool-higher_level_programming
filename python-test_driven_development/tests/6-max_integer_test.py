"""Unittest for max_integer([..])
"""
from configparser import MAX_INTERPOLATION_DEPTH
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_at_begining(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_in_middle(self):
        self.assertEqual(max_integer([3, 2, 4, 1]), 4)

    def test_one_neg(self):
        self.assertEqual(max_integer([3, 2, -4, 1]), 3)

    def test_all_neg(self):
        self.assertEqual(max_integer([-3, -2, -4, -1]), -1)

    def test_one_elem(self):
        self.assertEqual(max_integer([4]), 4)

    def test_empty(self):
        self.assertEqual(max_integer(), None)

    def test_emptylist(self):
        self.assertEqual(max_integer([]), None)

    def test_emptylist(self):
        with self.assertRaises(NameError):
            max_integer([a, 1, 2])

if __name__ == '__main__':
    unittest.main()()
