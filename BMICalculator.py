weight = int(input("How much do you weigh (lbs)? "))
height = int(input("How tall are you (inches)? "))



BMI = (weight / (height * height)) * 703
BMI_formatted = float((format(BMI, ".1f"))) #formats BMI to 1 decimal and keeps it as a float value

print("Your Body Mass Index is", BMI_formatted)

if BMI_formatted < 18.5:
    print("You are underweight.")
elif BMI_formatted >= 18.5 and BMI_formatted <= 24.9:
    print("You are a healthy weight.")
elif BMI_formatted >= 25 and BMI_formatted <= 29.9:
    print("You are overweight.")
elif BMI_formatted >= 30 and BMI_formatted <= 39.9:
    print("You are obese.")
elif BMI_formatted >= 40:
    print("You are morbidly obese.")
else:
    print("That number does not exist.")