#collect input 
#using length to know the number of string 
#the categorise the number of string
#using if statement 


string = len(input("enter string"))

if string < 5:
	print("short string")

elif string >= 5 and string <= 10:
	print("medium string")

else: 
	print("long string")