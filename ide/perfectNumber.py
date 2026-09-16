def perfect_square(numbers):
    results = [] 

    for number in numbers:
        square = False

        for root in range(1, number):
            if root * root == number:
                square = True;
                break
        results.append(square)
    return results

numbers = [4,9,25,49]
print(perfect_square(numbers))
    
