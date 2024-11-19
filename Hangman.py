import random

words = ["world", "family", "travel", "farming", "decisions", "house", "takeout", "party"]

word = random.choice(words)

chances = len(word) + 2

guesses = ''

while chances > 0:
    for char in word:
        print(char, end = " ")
        if char in guesses:
            print()
        else:
            print()