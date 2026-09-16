import unittest
from perfectNumber import*
class PerfectNumberTest(unittest.Testcase):

    def test_that_perfect_number_return_true(self):
    numbers = [4,9,25,49]

    expected = [True, True, True, True]

    actual = perfect_number(numbers)

    self.assertListEqual(expected, actual)
