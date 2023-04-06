heroes = {}

while True:
    input_str = input()

    if input_str == "End":
        break

    command, *args = input_str.split()

    if command == "Enroll":
        name = args[0]
        if name not in heroes:
            heroes[name] = []
        else:
            print(f"{name} is already enrolled.")

    elif command == "Learn":
        name, spell = args
        if name in heroes:
            if spell not in heroes[name]:
                heroes[name].append(spell)
            else:
                print(f"{name} has already learnt {spell}.")
        else:
            print(f"{name} doesn't exist.")

    elif command == "Unlearn":
        name, spell = args
        if name in heroes:
            if spell in heroes[name]:
                heroes[name].remove(spell)
            else:
                print(f"{name} doesn't know {spell}.")
        else:
            print(f"{name} doesn't exist.")

print("Heroes:")
for hero, spells in heroes.items():
    print(f"== {hero}: {', '.join(spells)}")