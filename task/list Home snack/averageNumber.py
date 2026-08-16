number = [23,45,56,67,12,34,87,35,45]

total = 0

average = 0

for count in range(len(number)):

    total += number[count]

average = total / count

print(average)
