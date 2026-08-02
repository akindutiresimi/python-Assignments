number = int(input("Enter number:"))
counter = 0
counters = 0
for count in range(1, number + 1, 1):

    if count % 2 == 0:
        counter = counter + 1
        
    else:
        counters = counters + 1
        
print("Even:", counter)
print ("odd:", counters)
