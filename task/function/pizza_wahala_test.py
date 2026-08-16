import unittest

from unittest import TestCase

from pizza_wahala import pizza_type, type


class PizzaTest(TestCase):

	def test_forPizzaType_isFour(self):

		expected_pizza_type = 0

		actual_pizza_type = pizza_type(4)

		self.assertEqual(actual_pizza_type, expected_pizza_type)




from account_function import check_balance, deposit