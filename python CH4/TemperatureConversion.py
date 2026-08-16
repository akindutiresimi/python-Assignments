def fahrenheit(celsius):
	fahrenheit = (9 / 5) * celsius + 32
	return fahrenheit




print ("celsius \t\t fahrenheit")
for celsius in range(0, 100 + 1):

    print("Celsius of", celsius, "\t\t", (fahrenheit(celsius)))
