import random

print("Rock, Paper, Scissors...")

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

userchoice = input("What do you choose? ")



if computer == "rock":
    if userchoice == "rock":
        print(f"The computer chose {computer}, You chose {userchoice}")
        print("Its a tie")
    elif userchoice == "paper":
        print(f"The computer chose {computer}, You chose {userchoice}")
        print("You Won!")
    elif userchoice == "scissors":
        print(f"The computer chose {computer}, You picked {userchoice}")
        print("You Lost!")
elif computer == "scissors":
    if userchoice == "rock":
        print(f"The computer chose {computer}, You chose {userchoice}")
        print("You Won!")
    elif userchoice == "paper":
        print(f"The computer chose {computer}, You chose {userchoice}")
        print("You Lost!")
    elif userchoice == "scissors":
        print(f"The computer chose {computer}, You chose {userchoice}")
        print("Its a tie!")
elif computer == "paper":
    if userchoice == "rock":
        print(f"The computer chose {computer}, You chose {userchoice}")
        print("You Lost!")
    elif userchoice == "paper":
        print(f"The computer chose {computer}, You chose {userchoice}")
        print("Its a tie!")
    elif userchoice == "scissors":
        print(f"The computer chose {computer}, You chose {userchoice}")
        print("You Won!")
