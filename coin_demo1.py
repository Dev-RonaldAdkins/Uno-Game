import random

class Coin:
    #__sideup creats a private attribute so it cannot be changed outside the class
    def __init__(self):
        self.__sideup = "Heads"

    
    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup

def main():

    my_coin = Coin()

    print("This side is up:", my_coin.get_sideup())

    print("I am tossing the coin...")
    my_coin.toss()


    print("This side is up:", my_coin.get_sideup())


main()
