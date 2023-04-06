password = input()

while True:
    data = input()
    if data == "Done":
        break
    new_raw_password = password
    splitted_data = data.split()
    command = splitted_data[0]
    if command == "TakeOdd":
        password = ""
        for letter in range(len(new_raw_password)):
            if letter % 2 != 0:
                password += new_raw_password[letter]

        print(password)
    elif command == "Cut":
        index = int(splitted_data[1])
        length = int(splitted_data[2])
        password = password.replace(password[index: index + length], "", 1)
        print(password)

    elif command == "Substitute":
        substring = splitted_data[1]
        substitute = splitted_data[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
print(f"Your password is: {password}")
