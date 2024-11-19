import random

#Asks for the users name
name = input("What is your name? ")
print ("Good luck " + name + "!")



words = ["light", "dark", "first", "cancel", "back", "upload", "pizza", "spaghetti"]



word = random.choice(words)     

#Has the uesr select a letter from the alphabet to start guessing the random word
print("Guess the characters")

guesses = ''

turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end = " ")
        else:
            print("_")
            failed +=1
    
    if failed == 0:
        print("You Win")
        print("The word is:", word)

    print()
    guess = input("Guess a character:")
    
    guesses += guess
    
    if guess not in word:
        turns -=1
        print("wrong")

        print("You have ", + turns, " more guesses")
        if turns == 0:
            print("You lost")





