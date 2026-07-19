#colllect a number 
#determine wether the number was palindrome 
#divide the number by modulus to single out them
#using if statement to compare each number
#print ass

number = int(input("enter number"))

number_one = int(number % 10)

numbers_two = int(number / 10)
number_two = int(numbers_two % 10)

numbers_three = int(number / 100)
number_three = int(numbers_three % 10) 
 
if number_one == number_three: 
	print("palindrome")

else: 
	print("not palindrome")