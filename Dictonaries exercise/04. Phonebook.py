phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone = entry.split("-")
    if name not in phonebook:
        phonebook[name] = phone
    else:
        phonebook[name] = phone
for check in range(int(entry)):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")