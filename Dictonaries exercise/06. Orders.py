product_dict = {}
quantity_dict = {}
while True:
    command = input()
    if command == "buy":
        break
    command_split = command.split()
    name = command_split[0]
    price = float(command_split[1])
    quantity = int(command_split[2])
    if name not in product_dict:
        product_dict[name] = price
        quantity_dict[name] = quantity

    else:
        product_dict[name] = price
        quantity_dict[name] += quantity


for name in product_dict:
    price = product_dict[name]
    quantity = quantity_dict[name]
    total_price = price * quantity
    print(f"{name} -> {total_price:.2f}")