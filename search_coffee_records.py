def main():

    found = False

    search = input("Enter a coffee name to search for: ")
    
    coffee_file = open("coffee.txt", "r")

    name = coffee_file.readline()

    while name != '':
        quantity = float(coffee_file.readline())

        name = name.strip("\n")

        if name == search:
            print("Name: ", name)
            print("Quantity", quantity)
            print()
            found = True

        name = coffee_file.readline()

    coffee_file.close()

    if not found:
        print("That item was not found in the file.")

main()