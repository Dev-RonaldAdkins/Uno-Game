
factorial = int(input("Enter the number to be factorialed: "))

while factorial < 0:
    print("That was not a valid input try again.")
    factorial = int(input("Enter the number to be factorialed: "))

total = 1   

for n in range(1, factorial + 1):
    total = n * total

print("The total is:", total)