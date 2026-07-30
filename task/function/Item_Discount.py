def apply_discount(item, original_price, promo_code):

    if promo_code == "SAVE10":
        dicount = 0.10
    elif promo_code == "HALFOFF":
        discount = 0.50
    else promo_code = "NO_VALID":
        no discount


    discounted = original - (original * discount)
    return dicounted


   print(apply_discount("bag", 200, "SAVE10"))
