food = input().split()
bakery = {}
for i in range(0, len(food), 2):
    key = food[i]
    value = int(food[i + 1])
    bakery[key] = value
print(bakery)