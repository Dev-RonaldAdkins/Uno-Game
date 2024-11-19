MAX = 5

total = 0.0

print("This program calculates the sum of", MAX, "numbers you will enter.")


for count in range(MAX):
    number = int(input('Enter a number: '))
    total += number

print("The total is", total)
