targets = [int(x) for x in input().split()]
is_valid = True
while True:
    line = input()
    splitted_data = line.split()
    command = splitted_data[0]
    if command == "Shoot":
        index = int(splitted_data[1])
        power = int(splitted_data[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif command == "Add":
        index = int(splitted_data[1])
        value = int(splitted_data[2])
        if index < 0 or index > len(targets):
            print("Invalid placement!")
        else:
            targets.insert(index, value)
    elif command == "Strike":
        index = int(splitted_data[1])
        radius = int(splitted_data[2])
        if index + radius >= len(targets) or index - radius < 0:
            print("Strike missed!")
        else:
            start_index = index - radius
            end_index = index + radius
            targets = targets[0:start_index] + targets[end_index + 1:len(targets)]

    elif command == "End":
        targets = [str(y) for y in targets]
        print("|".join(targets))
        break
