number = [23,45,56,67,12,34,87,35,45]

highest = number[0] 

for count in range(len(number)):

    if number[count] > highest:

        highest = number[count]

print(highest)
