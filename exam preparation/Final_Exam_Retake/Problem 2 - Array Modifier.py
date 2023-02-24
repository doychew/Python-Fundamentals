
integers = list(map(int, input().split()))
amount = 0
while True:
    commands = input()
    if commands == "end":
        break
    splitted_data = commands.split()
    command = splitted_data[0]

    if command == "swap":
        index1 = int((splitted_data[1]))
        index2 = int((splitted_data[2]))

        integers[index1], integers[index2] = integers[index2], integers[index1]

    elif command == "multiply":
        index1 = int(splitted_data[1])
        index2 = int(splitted_data[2])
        amount = integers[index1] * integers[index2]
        integers[index1] = amount

    elif command == "decrease":
        for i in range(len(integers)):
            integers[i] -= 1


integers = [str(x) for x in integers]
print(", ".join(integers))