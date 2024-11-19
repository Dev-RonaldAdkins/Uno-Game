score = 95

first_score = int(input("Enter the score of the first test: "))
second_score = int(input("Enter the score of the second test: "))
third_score = int(input("Enter the score of the third test: "))

average = (first_score + second_score + third_score) / 3
format_average = format(average, ".2f")


print("The average score is", format_average)

if average >= score:
    print("Congats! That is a great average")
else:
    print("Better luck next time.")
