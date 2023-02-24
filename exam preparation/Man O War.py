def is_valid_idx(idx, seq):
    return 0 <= idx < len(seq)


pirate_ship = [int(x) for x in input().split(">")]
warship = [int(y) for y in input().split(">")]
maximum_health_of_ship = int(input())

is_running = True
while is_running:
    line = input()
    if line == "Retire":
        break

    command_args = line.split()
    commands = command_args[0]

    if commands == "Fire":
        idx = int(command_args[1])
        damage = int(command_args[2])
        if not is_valid_idx(idx, warship):
            continue
        warship[idx] -= damage
        if warship[idx] <= 0:
            is_running = False
            print("You won! The enemy ship has sunken.")

    elif commands == "Defend":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        damage = int(command_args[3])
        if not is_valid_idx(start_idx, pirate_ship) or not is_valid_idx(end_idx, pirate_ship):
            continue
        for idx in range(start_idx, end_idx + 1):
            pirate_ship[idx] -= damage
            if pirate_ship[idx] <= 0:
                print("You lost! The pirate ship has sunken.")
                is_running = False
                break

    elif commands == "Repair":
        idx = int(command_args[1])
        health = int(command_args[2])

        if not is_valid_idx(idx, pirate_ship):
            continue
        pirate_ship[idx] = min(maximum_health_of_ship, pirate_ship[idx] + health)

    elif commands == "Status":
        treshold = maximum_health_of_ship * 0.2
        counter = 0
        for section in pirate_ship:
            if section < treshold:
                counter += 1

        print(f"{counter} sections need repair.")
if is_running:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
