import os

def main():
    found = False

    search = input("Enter a coffee name to delete: ")

    coffee_file = open("coffee.txt", "r")

    temp_file = open("temp.txt", "w")

    coffee_name = coffee_file.readline()

    while coffee_name != "":
        qty = float(coffee_file.readline())

        coffee_name = coffee_name.rstrip("\n")

        if coffee_name != search:
            temp_file.write(coffee_name + "\n")
            temp_file.write(str(qty) + "\n")
        else:
            found = True

        coffee_name = coffee_file.readline()

        coffee_file.close()
        temp_file.close()

        os.remove("coffee.txt")

        os.rename("temp.txt", "coffee.txt")

        if found:
            print("The file has been updated")
        else:
            print("That file does not exist")

main()


            

        