#ask the user for their age
#draft out a if statement 
#the if statement must contain 
#child age,teen and adult 
#print the categories the age  falls

age = int(input("enter age"))

if age > 0 and age <= 10:
	print("child")

if age > 11 and age <= 18:
	print("Teen")

if age > 18 and age <= 100:
	print("adult")



