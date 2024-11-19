import random
MIN = 1
MAX = 6

def main():
    roll = "y"

    while roll == "y":
        print("Rolling the dice....")
        print("The values are: ")
        print(random.randint(MIN,MAX))
        print(random.randint(MIN,MAX))
        roll = input("Would you like to roll again? (y/n) ").lower()
        


main()