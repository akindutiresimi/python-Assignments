#one
number = ["1", "2", "3"]
def convert_to_list(number):
    return int(number)

to_list = list(map(convert_to_list, number))
print("list result", to_list)


#2
number = [0,5,10,15]
def add_ten_to_list(number):
    return number + 10

add_list = list(map(add_ten_to_list, number))
print("add", add_list)


#3
temperature = [0, 20, 37, 100]
def convert_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

fahreniheit_list = list(map(convert_to_fahrenheit, temperature))
print("fahrenheit", fahreniheit_list)


#4
value = [1, None, 3, None, 5]
def remove_none_from_value(value):
    return value != None

none_from_list = list(filter(remove_none_from_value, value))
print("value", none_from_list)


#5
numbers = [1,3,4,6,9,12]
def extract_number_divisible_by_three(number):
    return number % 3 == 0

number_divisible_by_three = list(filter(extract_number_divisible_by_three, numbers))
print("number", number_divisible_by_three)



#6
number = [-2,-1,0,1,2]
def extract_only_positive_number(number):
    return number >= 0

positive_number = list(filter(extract_only_positive_number,number))
print("positive number", positive_number)




#7
details = [{'name': 'Alice', 'age': 30}, {'name': 'Bob','age': 20}]
def pick_the_age_greater_than_25(detail):
    return detail['age'] > 25

age_greater_than_25 = list(filter(pick_the_age_greater_than_25, details))
print("age", age_greater_than_25)






#8
numbers = [1,2,3,4,5]
from functools import reduce
def add_all_number(numbers, add):
    return numbers + add

addition = reduce(add_all_number, numbers)
print("addition", addition)


#9
numbers = [1,2,3,4,5]
from functools import reduce
def product_0f_all_number(numbers, product):
    return numbers * product

product = reduce(product_0f_all_number, numbers)
print("product", product)




#10
number = [3,7,2,9,1]
from functools import reduce 
def maximum_in_number(number, maximum):
    maximum = 0    
    return number > maximum

maximum = reduce(maximum_in_number, number)
print("maximum", maximum)









