#ask the weight from user 
#ask the height using input 
#use the BMI formua to calculate them together
#use the if statement to make then into condiction

weight = int (input("enter weight"))
height = int (input("enter height"))

BMI = int(weight / (height * height))

if BMI < 18.5:
	print("underweight")
elif BMI <= 24.9:
	print("normal")
elif BMI <= 29.9:
	print("overweigh")
else:
	print("obese")