#ask the total bill
#ask for memebership 
#using if statement to give condiction
#if the good is over 1000 and has membership discount of 10%
#but no membership discount 50%

total_bill = int(input("enter bill"))
is_member = input("are you a member")

if total_bill >=1000 and is_member =="yes":
	print("10% off")
elif total_bill >= 1000 and is_member != "yes": 
	print("5% off")
else:
	print("no discount")
