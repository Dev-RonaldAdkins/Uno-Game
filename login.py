def get_login_name(first, last, idnumber):

    first_slice = first[0:3]
    last_slice = last[0:3]
    id_slice = idnumber[-3:]


    login = first_slice + last_slice + id_slice

    return login



def valid_password(password):

    correct_length = False
    has_upper = False
    has_lower = False
    has_digit = False

    if len(password) >= 7:
        correct_length = True
        for char in password:
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_digit = True
    
    if correct_length == True and has_upper == True and has_lower == True and has_digit == True:
        is_valid = True
    else:
        is_valid = False
    
    return is_valid


    