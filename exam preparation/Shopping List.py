products = input().split("!")
while True:
    command_data = input()
    if command_data == "Go Shopping!":
        break
    command_data = command_data.split()
    command = command_data[0]
    item = command_data[1]
    if command == "Urgent" and item not in products:
        products.insert(0, item)
    elif command == "Unnecessary" and item in products:
        products.remove(item)
    elif command == "Correct":
        old_item = item
        new_item = command_data[2]
        if old_item in products:
            old_item_index = products.index(old_item)
            products[old_item_index] = new_item
    elif command == "Rearrange":
        if item in products:
            products.remove(item)
            products.append(item)
print(", ".join(products))


