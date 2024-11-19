import os

def main():

    found = False

    search = input("Enter a coffee name to search for: ")
    new_qty = int(input("Enter the new qty: "))

    coffee_file = open("coffee.txt", "r")

    temporary_file = open("temp.txt", "w")

    coffee_name = coffee_file.readline()

    while coffee_name != "":
        qty = float(coffee_file.readline())  

        coffee_name = coffee_name.rstrip("\n")

        if coffee_name == search:
            temporary_file.write(coffee_name + "\n")
            temporary_file.write(str(new_qty) + "\n")

            found = True
        else:
            temporary_file.write(coffee_name + "\n")
            temporary_file.write(str(qty) + "\n")

        coffee_name = coffee_file.readline()


    coffee_file.close()
    temporary_file.close()

    os.remove("coffee.txt")

    os.rename("temp.txt", "coffee.txt")

    if found:
        print("The file has been updated.")
    else:
        print("That item was not found in the file")

main()

    

            
