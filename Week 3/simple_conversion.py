#KILO_CONVERSION = 0.621371
MILES_CONVERSION = 1.60934


def convert_km_to_miles(kilometers, KILO_CONVERSION = 4):
    miles = kilometers * KILO_CONVERSION
    return miles

def convert_miles_to_kilometers(miles):
    kilometers = miles * MILES_CONVERSION
    return kilometers

def main():
    try:
        conversion = int(input("If you want to convert miles to kilometers enter 1. If you want kilometers to miles enter 2. "))
    
        if conversion == 1:
            miles_to_kilo = int(input("Enter the miles to be converted: "))
            print(miles_to_kilo, "miles converted to kilometers is", convert_miles_to_kilometers(miles_to_kilo))
        elif conversion == 2:
            kilo_to_miles = int(input("Enter kilometers to be converted: "))
            print(kilo_to_miles, "kilometers converted to miles is", convert_km_to_miles(kilo_to_miles))
        else:
            print("That is not a valid opton.")
    except:
         print("Enter a valid number")
main()



