
to_do_list = []

selection = input("Would you like to add to the list(add), delete an item(delete), or view the list(view)? ").lower()



while selection != "exit":
    if selection == "add":
        item = input("Type the item you would like to add. ")
        if item in to_do_list:
            print("This item is already in the list.")
            selection = input("Would you like to add to the list(add), delete an item(delete), view the list(view), or type exit to end the program? ").lower()
        else:
            to_do_list.append(item)
            print("The item has been added.")
            selection = input("Would you like to add to the list(add), delete an item(delete), view the list(view), or type exit to end the program? ").lower()

    elif selection == "delete":
        item = input("Type the item you would like to remove. ")
        if item in to_do_list:
            to_do_list.pop(item)
            print("The item has been removed.")
            selection = input("Would you like to add to the list(add), delete an item(delete), view the list(view), or type exit to end the program? ").lower()  

        else:
            print("That item is not in the list. Please try again.")
            selection = input("Would you like to add to the list(add), delete an item(delete), view the list(view), or type exit to end the program? ").lower() 

    elif selection == "view":
        if len(to_do_list) == 0:
            print("The to do list is empty.")
            selection = input("Would you like to add to the list(add), delete an item(delete), or type exit to end the program? ").lower()
        else:
            print(to_do_list)
            selection = input("Would you like to add to the list(add), delete an item(delete), or type exit to end the program? ").lower()
            
if selection == "exit":
    if len(to_do_list) == 0:
        print("The final to do list is empty")
    else:
        print("The final to do list is: " + str(to_do_list))