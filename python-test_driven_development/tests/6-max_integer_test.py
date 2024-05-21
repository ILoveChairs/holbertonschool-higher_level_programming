#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
        Spicer
    '''
    def test_no_arg(self):
        result = max_integer()
        self.assertEqual(result, None)

    def test_empty_list(self):
        result = max_integer([])
        self.assertEqual(result, None)

    def test_floats(self):
        result = max_integer([1.52, 6.3, 2.4])
        self.assertEqual(result, 6.3)

    def test_positive_ints(self):
        result = max_integer([7, 6, 5, 7, 255, 0])
        self.assertEqual(result, 255)
    
    def test_negative_ints(self):
        result = max_integer([-24, -247, -80, -74, -9, -245, -14])
        self.assertEqual(result, -9)


if __name__ == '__main__':
    unittest.main()
