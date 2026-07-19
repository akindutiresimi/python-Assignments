#using scanner to collect input of father age
#collect soon age too
#multiply the sons age by two
#subtract the father age from the son multiply age
#print th age


father = int(input("Enter father_age"))

son = int(input("Enter son_age"))

father_old_age = int(father - (son * 2))

if(father_old_age < 0):
	print("invalid")

else:
	print(father_old_age)
	
