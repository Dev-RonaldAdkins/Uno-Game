import math
import random

#User picks range of numbers for the random number to be between
userrange1 = int(input("What number you like to start with for your range? "))
userrange2 = int(input("What would you like to end the range with? "))

#Random integer between the range
randominteger = random.randint(userrange1, userrange2)

userguess = int(input("What would you like to guess the number is? "))

numberguesses = 0

while userguess is not randominteger:   
    if userguess > randominteger:
        print("Try again! You guessed too high.")
        userguess = int(input("What would you like to guess the number is? "))  
    elif userguess < randominteger:
        print("Try again! You guessed too low.")
        userguess = int(input("What would you like to guess the number is? "))  
    numberguesses += 1    

if numberguesses == 1:
    print("You have Won! You guessed the right number! It took you " + str(numberguesses) + " guess!")
else:
    print("You have Won! You guessed the right number! It took you " + str(numberguesses) + " guesses!")

        

