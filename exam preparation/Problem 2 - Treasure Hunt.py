lenght_loot = 0
treasure_list = []
treasure_chest = input().split("|")
while True:
    line = input()
    if line == "Yohoho!":
        break
    command_args = line.split()
    command = command_args[0]
    if command == "Loot":

        items = command_args[1:]
        for item in items:
            if item not in treasure_chest:
                treasure_list.insert(0, item)
    elif command == "Drop":
        index = int(command_args[1])
        if index + 1 > len(treasure_list):
            continue
        else:
            searched_element = treasure_list.pop(index)
            treasure_list.append(searched_element)
    elif command == "Steal":
        count_of_stolen_items = int(command_args[1])

        for i in range(count_of_stolen_items):
            if len(treasure_list) < count_of_stolen_items:
                treasure_list.pop()
            else:
                treasure_list.pop()
for x in treasure_list:
    lenght_loot += len(x)
chest_lenght = len(treasure_list)

print(treasure_list)
if len(treasure_list) <= 0:
    print("Failed treasure hunt.")
else:
    print(f"Average treasure gain: {lenght_loot / chest_lenght:.2f} pirate credits.")


