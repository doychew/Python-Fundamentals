cities = {}
while True:
    data = input()
    if data == "Sail":
        break
    new_data = data.split("||")
    city = new_data[0]
    population = int(new_data[1])
    gold = int(new_data[2])
    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
while True:
    line = input()
    if line == "End":
        break
    splitted_data = line.split("=>")
    command = splitted_data[0]
    if command == "Plunder":
        city = splitted_data[1]
        population = int(splitted_data[2])
        gold = int(splitted_data[3])
        current_poppulation = int(cities[city]["population"])
        current_gold = int(cities[city]["gold"])
        current_poppulation -= population
        current_gold -= gold
        if current_gold <= 0 or current_poppulation <= 0:
            print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
            print(f"{city} has been wiped off the map!")
            del cities[city]

        else:
            print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
            cities[city]["population"] = current_poppulation
            cities[city]["gold"] = current_gold
    elif command == "Prosper":
        city = splitted_data[1]
        gold = int(splitted_data[2])
        if gold < 0:
            print("Gold added cannot be a negative number!" )
        else:
            current_gold = int(cities[city]["gold"])
            current_gold += gold
            cities[city]['gold'] = current_gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
for city, value in cities.items():
    print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")