first_number = float(input("Enter first number: "))
operator = input("Select an operation (*, / , + , -) ")
second_number = float(input("Enter second number: "))


if operator == "*":
    answer = first_number * second_number
    print(format(answer, ","))
elif operator == "/":
    answer = first_number / second_number
    print(format(answer, ",.2f"))
elif operator == "+":
    answer = first_number + second_number
    print(answer)
elif operator == "-":
    answer = first_number - second_number
    print(answer)
else:
    print("That is not a valid operator.")

