class CheckOut:
    DISCOUNT_RATE = 0.075
    VAT = 0.17

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        if price < 0:
            raise ValueError("price cannot be negative")
        self.price = price

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("quantity cannot be less than zero")
        self.quantity = quantity

    def get_total(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.name:<15} Qty: {self.quantity:<5} price: #{self.price:<9.2f} Total: #{self.get_total():.2f}"

    @staticmethod
    def calculation_subtotal(cart):
        subtotal = 0
        for checkout in cart:
            subtotal += checkout.get_total()
        return subtotal

    @staticmethod
    def discount(subtotal):
        return subtotal * CheckOut.DISCOUNT_RATE

    @staticmethod
    def vat(subtotal):
        return subtotal * CheckOut.VAT

    @staticmethod
    def total(cart):
        subtotal = CheckOut.calculation_subtotal(cart)
        after_discount = subtotal - CheckOut.discount(subtotal)
        return after_discount + CheckOut.vat(after_discount)
