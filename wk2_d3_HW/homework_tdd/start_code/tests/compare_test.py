import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_2_4_returns_2_is_less_than_4(self):
        self.assertEqual("2 is less than 4", compare(2, 4))

    def test_compare_3_3_returns_3_is_equal_to_3(self):
        self.assertEqual("3 is equal to 3", compare(3, 3))        