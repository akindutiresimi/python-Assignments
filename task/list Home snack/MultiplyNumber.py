number = [23,45,56,67,12,34,87,35,45]


total = 1

for count in range(len(number)):


    if number[count] % 3 == 0:

        total += number[count]

print(total)

