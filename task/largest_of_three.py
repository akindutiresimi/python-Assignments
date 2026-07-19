#ask for three integer
#using if statement to find 
#the largest of the number

a = int (input("enter number"))
b = int (input("enter number"))
c = int (input("enter number"))

if a > b and a > c:
	print ("a")
if b > a and b > c:
	print ("b")
else:
	print("c")