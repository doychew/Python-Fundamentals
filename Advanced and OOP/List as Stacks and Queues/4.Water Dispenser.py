from collections import deque
quantity = int(input())
name = input()
water_line = deque()
while name != "Start":
    water_line.append(name)
    name = input()
command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        litters_to_give = int(data[0])
        if quantity >= litters_to_give:
            print(f"{water_line.popleft()} got water")
            quantity -= litters_to_give

        else:
            print(f"{water_line.popleft()} must wait")

    else:
        litters_to_fill = int(data[1])
        quantity += litters_to_fill
    command = input()
print(f"{quantity} liters left")