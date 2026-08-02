number = int(input("Enter number"))

counter = 0
for count in range(1, 100):

    if count % number == 0:

        counter = counter + 1

print(counter) 
