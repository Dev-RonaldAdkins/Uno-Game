
def main():
    numbers = [2, 4, 6, 8, 10]

    #acumulator variable
    total = 0

    for value in numbers:
        total += value

    average = total / (len(numbers))    
    
    print("The total of the elements is", total)
    print("The average of the elemets is", average)


main()
