message = input()
while True:
    data = input()
    if data == "Decode":
        break
    splitted_data = data.split("|")
    command = splitted_data[0]
    if command == "Move":
        number_of_letters = int(splitted_data[1])
        message = message[number_of_letters:] + message[:number_of_letters]
    elif command == "Insert":
        index = int(splitted_data[1])
        value = (splitted_data[2])
        message = message[:index] + value + message[index:]
    elif command == "ChangeAll":
        substring = splitted_data[1]
        replacement = splitted_data[2]
        message = message.replace(substring, replacement)
print(f"The decrypted message is: {message}")
