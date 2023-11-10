from collections import deque

fuel = [int(x) for x in input().split()]
consumption = deque([int(x) for x in input().split()])
altitude = deque([int(x) for x in input().split()])

counter = 0
has_reached_any = False

while fuel and consumption:
    current_fuel = fuel.pop()
    current_consumption = consumption.popleft()
    current_altitude = altitude.popleft()
    counter += 1
    temp = current_fuel - current_consumption

    if temp >= current_altitude:
        has_reached_any = True
        print(f"John has reached: Altitude {counter}")
    else:
        print(f"John did not reach: Altitude {counter}")
        print("John failed to reach the top.")
        if has_reached_any:
            print("Reached altitudes:", end=' ')

            reached_altitudes = [f"Altitude {i}" for i in range(1, counter)]
            print(", ".join(reached_altitudes))
        else:
            print("John didn't reach any altitude.")
        break

    if not altitude:
        print("John has reached all the altitudes and managed to reach the top!")
        break
