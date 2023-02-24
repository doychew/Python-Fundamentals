coffee_names = input().split()
number_of_commands = int(input())
for i in range(number_of_commands):
    line = input()
    splited_data = line.split()
    command = splited_data[0]
    if command == "Include":
        coffee = splited_data[1]
        coffee_names.append(coffee)
    elif command == "Remove":
        cofee_removes = splited_data[1]
        number_of_coffees = int(splited_data[2])

        if number_of_coffees > len(coffee_names):
            continue
        else:
            if cofee_removes == "first":
                coffee_names = coffee_names[number_of_coffees:]
            elif cofee_removes == "last":
                for i in range(number_of_coffees):
                    coffee_names.pop()
    elif command == "Prefer":
        index1 = int(splited_data[1])
        index2 = int(splited_data[2])
        if 0 <= index1 < len(coffee_names) and 0 <= index2 < len(coffee_names):
            coffee_names[index1], coffee_names[index2] = coffee_names[index2], coffee_names[index1]
        else:
            continue
    elif command == "Reverse":
        coffee_names = coffee_names[::-1]

print(f"Coffees:\n"
      f"{' '.join(coffee_names)}")




