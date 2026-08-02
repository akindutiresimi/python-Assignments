def apply_discount(item, original_price, promo_code):

    if promo_code == "SAVE10":
        discount = 0.10
    elif promo_code == "HALFOFF":
        discount = 0.50
    else:
        discount = 0


    discounted = original_price - (original_price * discount)
    return discounted

print(apply_discount("bag", 400, "no discount"))

