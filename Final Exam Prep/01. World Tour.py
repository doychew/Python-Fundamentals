stops = input()
while True:
    data = input()
    if data == "Travel":
        break
    splitted_data = data.split(":")
    command = splitted_data[0]
    if command == "Add Stop":
        index = int(splitted_data[1])
        string = splitted_data[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif command == "Remove Stop":
        start_index = int(splitted_data[1])
        end_index = int(splitted_data[2])
        if 0 <= start_index < len(stops) and  0 <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)
    elif command == "Switch":
        old_string = splitted_data[1]
        new_string = splitted_data[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)
print(f"Ready for world tour! Planned stops: {stops}")