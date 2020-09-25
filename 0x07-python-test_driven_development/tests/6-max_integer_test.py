#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

ma = [2, 3, 4, 5]


class TestMaxInteger(unittest.TestCase):
    """class max integer"""
    def test_max_integer(self):
        """# test max in a list"""
        self.assertEqual(max_integer(ma), 5)

    def test_empty_list(self):
        """test when empty list"""
        self.assertEqual(max_integer([]), None)

    def test_is_list(self):
        """test to verify if is a list"""
        assert(isinstance(ma, list))

    def test_list_integers(self):
        for num in ma:
            assert(isinstance(num, int))

if __name__ == '__main__':
    unittest.main()
