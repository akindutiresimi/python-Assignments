class CheckOut:
    DISCOUNT_RATE = 0.075
    VAT = 0.17

    def ( name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name():
        return name

    def get_price():
        return price

    def get_quantity():
        return quantity

    def set_name(name):
        self.name = name

    def set_price(price):
        if price < 0:
            raise ValueError("price cannot be negative")
        self.price = price

    def set_quantity(quantity):
        if quantity < 0:
            raise ValueError("quantity cannot be less than zero")
        self.quantity = quantity

    def get_total(self):
        return quantity * price

    def str():
        return f"{name:<15} Qty: {quantity:<5} price: #{price:<9.2f} Total: #{get_total():.2f}"

    def calculation_subtotal(cart):
        subtotal = 0
        for checkout in cart:
            subtotal += checkout.get_total()
        return subtotal

    def discount(subtotal):
        return subtotal * CheckOut.DISCOUNT_RATE

    def vat(subtotal):
        return subtotal * CheckOut.VAT

    def total(cart):
        subtotal = CheckOut.calculation_subtotal(cart)
        after_discount = subtotal - CheckOut.discount(subtotal)
        return after_discount + CheckOut.vat(after_discount
