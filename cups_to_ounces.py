def main():
    #display intro screen
    intro()
    #Get number of cups
    cups_needed = int(input("Enter the number of cups to convert to fluid ounces: "))
    #Convert cups to ounces
    cups_to_ounces(cups_needed)



#To display introduction screen
def intro():
    print("This program will help you convert the number of cups to fluid ounces. The number of cups in an ounce is 8.")
    print()

#Accepts number of cups to convert and displays the equivalent in ounces
def cups_to_ounces(cups):
    ounces = cups * 8
    print("That converts to", ounces, "ounces")

main()