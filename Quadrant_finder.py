#ask for two integer
#using if statment to 
#make condiction out of the integer  

x = int(input("enter integer"))

y = int(input("enter integer"))

if x > 0 and y > 0:
	print("Q1")
elif x < 0 and y > 0:
	print("Q2")
elif x < 0 and y < 0:
	print("Q3")
elif x > 0 and y < 0:
	print("Q4")
elif x == 0 and y == 0:
	print("Origin")
elif x !=0 and y == 0:
	print("X-axis")
else:
	print("Y-axis") 