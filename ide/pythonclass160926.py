#like_foods = ["Rice", "Cocoyam", "Spag", "Noodle"]
#foods = ["Rice", "Egusi", "Okpa", "Beans", "Garri", "Amala", "Spag"]
#
#def is_food_not_liked(food):
#    return food_is_not_liked_food
#
#unliked_foods = list(filter(is_food_not_liked,foods))
#print("linked food are", unliked_foods)
#print("liked food", liked_foods)
#print("all food", foods)
#



#
#text = "Hello Semicolon Nature"
#
#def is_upper_case(letter):
#    return letter == letter.lower()
#
#upper_cased_letters = list(filter(is_upper_case, text))
#print("upper", upper_cased_letters)
#


#
#number = [1,2,3,4,5,6,7,8,9,10]
#
#def is_even_number(number):
#    return number % 2 != 0
#
#even_number = list(filter(is_even_number, number))
#print("even", even_number)
#
#

#
#number = [4,9,8,21,49,2]
#
#def is_perfect_square(number):
#    return (number * 0.5) % 1 == 0
#
#print(map(is_perfect_square, number))
#
#
#



number = [4,7,8,39,78,13]
from functools import reduce


def sum_up(accumulator, number):
    return accumulator + number
    
result = reduce(sum_up, number)

print(result)
















