import random

num_dice = int(input("How many dice would you like to roll? (1, 2, 3, or 4) "))

roll_dice1 = random.randint(1,6)
roll_dice2 = random.randint(1,6)
roll_dice3 = random.randint(1,6)
roll_dice4 = random.randint(1,6)

while num_dice < 1 or num_dice > 4:
    print("That is not a valid number of dice.")
    num_dice = int(input("How many dice would you like to roll? (1, 2, 3, or 4) "))

if num_dice == 1:
    print("You rolled", roll_dice1)
elif num_dice == 2:
    first_dice = roll_dice1
    second_dice = roll_dice2
    print("First dice:", first_dice)
    print("Second dice:", second_dice)
    print("Total is:" , first_dice + second_dice)
elif num_dice == 3:
    first_dice = roll_dice1
    second_dice = roll_dice2
    third_dice = roll_dice3
    print("First dice:", first_dice)
    print("Second dice:", second_dice)
    print("Third dice:", third_dice)
    print("Total is:", first_dice + second_dice + third_dice)
elif num_dice == 4:
    first_dice = roll_dice1
    second_dice = roll_dice2
    third_dice = roll_dice3
    fourth_dice = roll_dice4
    print("First dice:", first_dice)
    print("Second dice:", second_dice)
    print("Third dice:", third_dice)
    print("Fourth dice:", fourth_dice)
    print("Total is:" , first_dice + second_dice + third_dice + fourth_dice)
