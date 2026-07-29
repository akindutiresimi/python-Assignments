for number in range(1, 5, 1):
    if number % 4 == 0:
        sumOne = number + number ** 2 + number ** 3 + number ** 4 + number ** 5
        #print(sumOne)

for numberTwo in range(1, 11, 1):
    if numberTwo % 8 == 0:
        sumTwo = numberTwo + numberTwo ** 2 + numberTwo ** 3 + numberTwo ** 4 + numberTwo ** 5
        #print(sumTwo)
        sumTotal =  sumOne + sumTwo
        print("sumTotal:", sumOne + sumTwo)
 
        print("sum_Square:", sumTotal **2)
