number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def addDesignatedFunction(number):

    total = 0

    for count in range(len(number)):

        if number[count] % 3 == 0:

            total += number[count]   

    return total





print(addDesignatedFunction(number))
