KILOMETERS_VARIABLE = 0.6214

def main():
    kilometers = int(input("Enter the number of Kilometers: "))
    print(kilometers, " kilometers converted to miles is", format(convert_killometers_to_miles(kilometers), ".2f"))

def convert_killometers_to_miles(kilo):
    miles = kilo * KILOMETERS_VARIABLE
    return miles

main()