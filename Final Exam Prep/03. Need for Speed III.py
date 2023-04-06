cars = {}
max_fuel = 75
number_of_cars = int(input())
for i in range(number_of_cars):
    line = input().split("|")
    car = line[0]
    mileage = int(line[1])
    fuel = int(line[2])
    cars[car] = {'mileage': mileage, "fuel": fuel}
while True:
    data = input()
    if data == "Stop":
        break
    splitted_data = data.split(" : ")
    command = splitted_data[0]

    if command == "Drive":
        car = splitted_data[1]
        distance = int(splitted_data[2])
        fuel = int(splitted_data[3])
        if fuel > cars[car]['fuel']:
            print("Not enough fuel to make that ride")
        else:
            cars[car]['fuel'] -= fuel
            cars[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]['mileage'] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]
    elif command == "Refuel":
        car = splitted_data[1]
        fuel = int(splitted_data[2])
        if fuel > max_fuel - int(cars[car]['fuel']):
            current_fuel = int(cars[car]['fuel'])
            print(f"{car} refueled with {max_fuel - current_fuel} liters")
            current_fuel += max_fuel - current_fuel
            cars[car]["fuel"] = current_fuel
        else:
            cars[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif command == "Revert":
        car = splitted_data[1]
        kilometers = int(splitted_data[2])
        current_mileage = int(cars[car]['mileage'])
        current_mileage -= kilometers
        if cars[car]['mileage'] < 10000:
            cars[car]['mileage'] = 10000
        print(f"{car} mileage decreased by {kilometers} kilometers")
        cars[car]['mileage'] = current_mileage
for car, value in cars.items():
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")





