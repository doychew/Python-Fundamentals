password = input()
is_not_valid = False
while True:
    data = input()
    if data == "Complete":
        break
    splitted_data = data.split()
    command = splitted_data[0]
    if command == "Make" and splitted_data[1] == "Upper":
        index = int(splitted_data[2])
        if 0 <= index < len(password):
            password = password[:index] + password[index].upper() + password[index+1:]
            print(password)
    elif command == "Make" and splitted_data[1] == "Lower":
        index = int(splitted_data[2])
        if 0 <= index < len(password):
            password = password[:index] + password[index].lower() + password[index + 1:]
            print(password)
    elif command == "Insert":
        index = int(splitted_data[1])
        char = splitted_data[2]
        if 0 <= index < len(password):
            password = password[:index] + char + password[index:]
            print(password)
    elif command == "Replace":
        char = splitted_data[1]
        value = int(splitted_data[2])
        if char in password:
            sum = int(ord(char) + value)
            char1 = chr(sum)
            password = password.replace(char, char1)
            print(password)
    elif command == "Validation":
        if len(password) <= 8:
            print("Password must be at least 8 characters long!")
        for character in password:
            if not character.isalnum() and character != "_":
                is_not_valid = True
        if is_not_valid:
            print(f"Password must consist only of letters, digits and _!")

        if not any(x.isupper() for x in password):
            print("Password must consist at least one uppercase letter!")
        if not any(y.islower() for y in password):
            print("Password must consist at least one lowercase letter!")
        if not any(z.isdigit() for z in password):
            print(f"Password must consist at least one digit!")