
#collect three input from user
#using if else statement 
#input the numerical score range 
#print the grade after each if statement 
#add the three number together then divid by three
#print the average of the score.


score_one = int(input("Enter score_one"))

score_two = int(input("Enter score_two")) 

score_three = int(input("Enter score_three"))

Score = int((score_one + score_two + score_three) / 3)


if 90 <= Score <= 100:
	print ("A")

elif 80 <= Score < 90:
	print ("B")

elif 70 <= Score < 80:
	print ("C")

elif 60 <= Score < 70:
	print ("D")

else:
	print ("F")


	



