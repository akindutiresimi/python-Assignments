number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def addFirstMiddleLastNumber(number):

    total = 0


    total += number[0] + number[8] + number[14]

            

    return total



print(addFirstMiddleLastNumber(number))
