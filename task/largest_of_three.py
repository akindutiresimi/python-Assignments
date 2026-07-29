#ask for three integer
#using if statement to find 
#the largest of the number

number_one = int (input("enter number"))
number_two = int (input("enter number"))
number_three = int (input("enter number"))

if number_one > number_two and number_one > number_three:
	print ("number_one")
if number_two > number_one and number_two > number_three:
	print ("number_two")
else:
	print("number_three")
