def main():
    coffee_file = open("coffee.txt", "r")

    name = coffee_file.readline()

    while name != '':
        quantity = coffee_file.readline()

        name = name.rstrip("\n")
        quanity = quantity.rstrip("\n")

        print("Coffee name: ", name)
        print("Quantity: ", quanity, "pounds")
        print()

        name = coffee_file.readline()

    coffee_file.close()

main()
