message = input()
while True:
    data = input()
    if data == "Reveal":
        break
    splitted_data = data.split(":|:")
    command = splitted_data[0]
    if command == "InsertSpace":
        index = int(splitted_data[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif command == "Reverse":
        substring = splitted_data[1]
        if substring in message:
            reversed_substring = substring[::-1]
            message = message.replace(substring, "", 1)
            message += reversed_substring
            print(message)
        else:
            print('error')
    elif command == "ChangeAll":
        substring = splitted_data[1]
        replacement = splitted_data[2]
        message = message.replace(substring, replacement)
        print(message)
print(f"You have a new text message: {message}")