
def main():
    scores = get_scores()

    total = get_total(scores)

    lowest = min(scores)

    total -= lowest

    average = total / (len(scores) - 1)

    print("The average with the lowest score dropped is", average)


def get_scores():

    again = "y"
    scores = []

    while again == "y" or again == "Y":
        grade = float(input("Please enter the score of the exam: "))

        scores.append(grade)
        again = input("Do you have more scores to enter? (y/n) ")
        print()
    
    return scores


def get_total(grade_list):
    total = 0.0

    for num in grade_list:
        total += num
    
    return total


main()


    
