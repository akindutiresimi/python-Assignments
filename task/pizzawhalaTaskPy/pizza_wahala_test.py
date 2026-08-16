#import unittest

from unittest import Testcase

from account_function import


class PizzaTest(TestCase):

	def test_forPizzaType_isFour(self):

		expected_pizza_type = 0

		actual_pizza_type = pizza_type(4)

		self.assertEqual(actual_pizza_type, expected_pizza_type)




