import random

def main():
    even_count = 0
    odd_count = 0
    for currentIteration in range(1, 101):
        random_number = generateRandomNumber()
        if odd_or_even(random_number):
            even_count += 1
        else:
            odd_count +=1

    printResults(even_count, odd_count)

def printResults(even_count, odd_count):
    print("Out of one hunrded, there were", even_count, "even numbers and", odd_count,"odd numbers")
        

def generateRandomNumber():
    random_number = random.randint(1,10)
    return random_number


def odd_or_even(number):
    if number % 2 == 0:
       return True
    return False
       


main()