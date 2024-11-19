def main():
    number = int(input("Enter the number to be multiplied by ten: "))
    print("The number you entered multiplied by 10 is: ", times_ten(number))


def times_ten(number):
    product = number * 10
    return product

main()

