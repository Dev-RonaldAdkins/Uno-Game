import login

def main():

    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    idnumber = input("Enter your student ID number: ")

    print("Your system login name is:")
    print(login.get_login_name(first, last, idnumber))


main()