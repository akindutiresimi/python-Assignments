import unittest
from checkout import CheckOut


class CheckOutTest(unittest.TestCase):

    def setUp(self):
        self.check_out = CheckOut("bottle water", 400, 2)

    def test_that_the_product_bought_by_a_client(self):
        self.assertEqual("bottle water", self.check_out.get_name())

    def test_that_the_product_the_customer_bought_is_soso_amount(self):
        self.assertEqual(400, self.check_out.get_price())

    def test_that_the_product_the_customer_pick(self):
        self.assertEqual(2, self.check_out.get_quantity())

    def test_that_the_customer_pick_more_water(self):
        self.check_out.set_price(1000)
        self.assertEqual(1000, self.check_out.get_price())

    def test_that_the_customer_pick_another_product(self):
        self.check_out.set_name("Spray")
        self.assertEqual("Spray", self.check_out.get_name())

    def test_that_the_customer_pick_set_of_spray(self):
        self.check_out.set_quantity(7)
        self.assertEqual(7, self.check_out.get_quantity())

    def test_the_calculation_of_all_goods_bought(self):
        self.assertEqual(800, self.check_out.get_total())

    def test_that_the_product_where_all_group_to_according_item(self):
        cart = [
            CheckOut("bottle water", 400.0, 2),
            CheckOut("spray", 1000.0, 7),
        ]
        subtotal = CheckOut.calculation_subtotal(cart)
        self.assertEqual(7800.0, subtotal)

    def test_that_the_product_where_all_item_is_empty(self):
        cart = []
        subtotal = CheckOut.calculation_subtotal(cart)
        self.assertEqual(0, subtotal)

    def test_that_the_discount_to_the_product(self):
        discount = CheckOut.discount(800)
        self.assertEqual(60, discount)

    def test_that_the_discount_wont_function_when_the_customer_cart_no_product(self):
        discount = CheckOut.discount(0)
        self.assertEqual(0, discount)

    def test_the_vat_of_the_item_cart_by_the_customer(self):
        vat = CheckOut.vat(800)
        self.assertEqual(136, vat)

    def test_that_the_total_amount_after_discount_has_been_removed_and_vat_has_been_added(self):
        cart = [
            CheckOut("bottle water", 400.0, 2),
            CheckOut("spray", 1000, 7),
        ]
        total = CheckOut.total(cart)
        self.assertAlmostEqual(8441.55, total)

    def test_that_the_total_amount_after_discount_has_been_removed_and_vat_has_been_added_to_a_new_product(self):
        cart = [
            CheckOut("milk", 2100.0, 2),
            CheckOut("spray", 550, 2),
        ]
        total = CheckOut.total(cart)
        self.assertAlmostEqual(5735.925, total)


if __name__ == "__main__":
    unittest.main()
