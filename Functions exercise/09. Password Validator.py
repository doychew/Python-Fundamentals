def password_validation(some_password):
    is_valid = True
    if len(some_password) < 6 or len(some_password) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not some_password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    digit_counter = 0
    for character in some_password:
        if character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    return is_valid
password = input()
password_is_valid = password_validation(password)
if password_is_valid:
    print("Password is valid")