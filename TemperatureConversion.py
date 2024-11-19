user_conversion = int(input("What would you like to convert to? Celsius(1) or Farenheit(2)? Type '1' or '2'. "))

def conversion_to_farenheit(temperature_to_farenheit):
    conversion = (temperature_to_farenheit * (9/5)) + 32
    print("Your temp in farenheit is", conversion, "degrees")

def conversion_to_celsius(temperature_to_celsius):
    conversion = (temperature_to_celsius-32) * (5/9)
    print("Your temp in farenheit is", conversion, "degrees")

if user_conversion == 1:
    temperature_to_celsius = int(input("What is the Farenhiet temperature you would like to convert? "))
    conversion_to_celsius(temperature_to_celsius)
           
elif user_conversion == 2:
    temperature_to_farenheit = int(input("What is the Celsius temperature you would like to convert? "))
    conversion_to_farenheit(temperature_to_farenheit)
else:
    print("That is not a valid input.")
    
