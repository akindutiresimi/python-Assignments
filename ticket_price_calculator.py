#ask for the 
#using and if and elif
#we use the if to condiction 
#the entering 
#that i if the aage 
#is less than 5 free
#and so on



age = int(input("enter age"))

if age < 5:
	print("free")
elif age <= 12:
	print("$5")  
elif 13 >= age <= 64:
	print("$12")
else:
	print("$8")