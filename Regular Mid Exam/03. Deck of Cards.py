cards = input().split(", ")
number_of_commands = int(input())
for i in range(number_of_commands):
    line = input()
    splited_data = line.split(", ")
    command = splited_data[0]
    if command == "Add":
        cardname = splited_data[1]
        if cardname in cards:
            print("Card is already in the deck")
        elif cardname not in cards:
            cards.append(cardname)
            print("Card successfully added")
    elif command == "Remove":
        cardname = splited_data[1]
        if cardname in cards:
            cards.remove(cardname)
            print("Card successfully removed")
        elif cardname not in cards:
            print("Card not found")
    elif command == "Remove At":
        index = int(splited_data[1])
        if index < 0 or index >= len(cards):
            print("Index out of range")
        else:
            cards.pop(index)
            print("Card successfully removed")
    elif command == "Insert":
        index = int(splited_data[1])
        cardname = splited_data[2]
        if index < 0 or index >= len(cards):
            print("Index out of range")
        elif 0 <= index < len(cards) and cardname in cards:
            print("Card is already added")
        elif 0 <= index < len(cards) and cardname not in cards:
            cards.insert(index, cardname)
            print("Card successfully added")
print(', '.join(cards))




