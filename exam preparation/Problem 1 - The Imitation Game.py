message = input()
while True:
    message = list(message)
    commands = input()
    if commands == "Decode":
        break
    commands = commands.split("|")
    command = commands[0]
    if command == "Move":

        number_of_letters = int(commands[1])

        for i in range(number_of_letters):
            removed_letter = message.pop(0)
            message.append(removed_letter)

    elif command == "Insert":
        index = int(commands[1])
        value = commands[2]
        message.insert(index, value)
    elif command == "ChangeAll":
        message = "".join(message)
        substring = commands[1]
        replacement = commands[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {''.join(message)}")
