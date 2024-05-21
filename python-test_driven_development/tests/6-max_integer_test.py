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

    def test_one_element(self):
        result = max_integer([69])
        self.assertEqual(result, 69)

    def test_floats(self):
        result = max_integer([1.52, 6.3, 2.4])
        self.assertEqual(result, 6.3)

    def test_max_at_middle(self):
        result = max_integer([7, 6, 5, 7, 255, 0])
        self.assertEqual(result, 255)
    
    def test_negative_ints(self):
        result = max_integer([-24, -247, -80, -74, -9, -245, -14])
        self.assertEqual(result, -9)

    def test_max_at_start(self):
        result = max_integer([1000, 20, 10, 25, 45])
        self.assertEqual(result, 1000)

    def test_max_at_end(self):
        result = max_integer([20, 10, 25, 45, 1000])
        self.assertEqual(result, 1000)


if __name__ == '__main__':
    unittest.main()
