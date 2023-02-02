water_tank_capacity = 255
capacity = 0
n = int(input())
for i in range(n):
    liter_water = int(input())

    if capacity + liter_water > water_tank_capacity:
        print("Insufficient capacity!" )
    else:
        capacity += liter_water
print(capacity)