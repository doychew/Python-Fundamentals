license_plate_by_username = {}
count = int(input())
for i in range(count):
    data = input()
    command_split = data.split()
    command = command_split[0]
    name = command_split[1]
    if command == "register":
        license_plate = command_split[2]
        if name not in license_plate_by_username:
            license_plate_by_username[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif command == "unregister":
        if name not in license_plate_by_username:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del license_plate_by_username[name]
for name, license_plate in license_plate_by_username.items():
    print(f"{name} => {license_plate}")
