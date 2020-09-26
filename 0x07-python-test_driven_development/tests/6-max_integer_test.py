#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class max integer"""
    def test_max_integer(self):
        """# test max in a list"""
        ma = [2, 3, 4, 5]
        self.assertEqual(max_integer(ma), 5)

    def test_empty_list(self):
        """test when empty list"""
        self.assertIsNone(max_integer([]))

    def test_compare_string(self):
        """test case compare strings"""
        self.assertEqual(max_integer(["Daniel", "Villalba"]), "Villalba")

    def test_None_list(self):
        """Test case None in List"""
        self.assertIsNone(max_integer([None]))

    def test_no_arguments(self):
        """test if the item is a int"""
        self.assertIsNone(max_integer())


class TestExpectedFailure(unittest.TestCase):
    """class for expected failures in execution"""
    @unittest.expectedFailure
    def test_booleans(self):
        """to avoid the error of raise"""
        self.assertEqual(max_integer([False, True]), False)

    def test_string_in_list(self):
        with self.assertRaises(TypeError):
            max_integer(["Daniel", 1, 2, 3])

    def test_too_Arguments(self):
        with self.assertRaises(TypeError):
            max_integer([3, 2, 7], [2, 4, 5])

    def test_with_set(self):
        """test when is a set"""
        with self.assertRaises(TypeError):
            max_integer({3, 6, 5, 1})
    # test for cases with None's

    def test_case_None(self):
        """test case for unique None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_case_2None(self):
        """test case list of None"""
        with self.assertRaises(TypeError):
            max_integer([None, None])

    def test_case_3None(self):
        """test case none and int in list"""
        with self.assertRaises(TypeError):
            max_integer([6, None, 3])


if __name__ == '__main__':
    unittest.main()
