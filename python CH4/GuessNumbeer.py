import random 

def number_guess():

    guess = random.randrange(1, 1000)

    print(guess)

    print("guess the number between 1 to 1000 with fewer guess")


    while(True):

        number = int(input("Enter your guess number"))

        if number > guess:

            print("incorrect, Too high")

        elif number < guess:

            print("incorrect, too low")

        else:   

            print("congratulation you guess right")




        for (int count = 0; count < number; count ++){

            if number == guess:

            print(number[count]);
        }
            break


while (True):

    number_guess()

    number_guess = input("Do you want to play again(yes/no)")

    if(number_guess != "yes" or number_guess == "no" or number_guess != "y" or number_guess != "n"):

        print("Thanks")

        break




      
