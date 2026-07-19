#ask a user to enter a letter
#use if statement to make the condiction.
#if it a letter print vowel else constant


letter = input("enter a leter")

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
	print("Viowel")

elif letter != "a" or letter != "e" or letter != "i" or letter != "o" or letter != "u":
	print("Consonant")

else:
	print("invalid input")

	