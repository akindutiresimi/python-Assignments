number = [23,45,56,67,12,34,87,35]

total = 0

for count in range(len(number)):


    if count % 2 != 0:

        total += number[count]

print(total)

