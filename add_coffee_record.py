
def main():
    another = "y"

    coffee_file = open("coffee.txt", "a")
 
    while another == "Y" or another == "y":
        name_coffee = input("Enter the name of the coffee: ")
        try:
            quantity_coffee = float(input("Enter the number of pounds: "))
            coffee_file.write(name_coffee + "\n")
            coffee_file.write(str(quantity_coffee) + "\n")
        except:
            print("That is not a valid input. Item was not added.")
        another = input("Would you like to add an item to your inventory? (y/n)")
    
    coffee_file.close()
    print("The coffee inventory has been added to coffee.txt")

main()