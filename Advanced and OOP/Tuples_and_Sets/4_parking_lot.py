n = int(input())
parking_cars = set()
for _ in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        if car_number not in parking_cars:
            parking_cars.add(car_number)
    elif direction == "OUT":
        if car_number in parking_cars:
            parking_cars.remove(car_number)
if len(parking_cars) == 0:
    print("Parking Lot is Empty")
else:
    print("\n".join(parking_cars))