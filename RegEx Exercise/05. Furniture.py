import re

pattern = r"^>>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)$"

total_price = 0
bought_items = []
while True:
    line = input()
    if line == "Purchase":
        break

    match = re.findall(pattern, line)
    if not match:
        continue

    groups = match[0]

    item = groups[0]
    price = float(groups[1])
    quantity = int(groups[3])

    bought_items.append(item)
    total_price += price * quantity

print(f"Bought furniture:")
for product in bought_items:
    print(product)
print(f"Total money spend: {total_price:.2f}")