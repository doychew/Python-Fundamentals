raw_activation_key = input()
while True:
    data = input()
    if data == "Generate":
        break
    splitted_data = data.split(">>>")
    command = splitted_data[0]
    if command == "Contains":
        substring = splitted_data[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print(f"Substring not found!")
    elif command == "Flip":
        command2 = splitted_data[1]
        if command2 == "Upper":
            start_index = int(splitted_data[2])
            end_index = int(splitted_data[3])
            raw_activation_key = raw_activation_key[0:start_index] + raw_activation_key[
                                                                 start_index:end_index].upper() + raw_activation_key[
                                                                                                  end_index:]
        elif command2 == "Lower":
            start_index = int(splitted_data[2])
            end_index = int(splitted_data[3])
            raw_activation_key = raw_activation_key[0:start_index] + raw_activation_key[
                                                                 start_index:end_index].lower() + raw_activation_key[
                                                                                                  end_index:]
        print(raw_activation_key)
    elif command == "Slice":
        start_index = int(splitted_data[1])
        end_index = int(splitted_data[2])
        raw_activation_key = raw_activation_key[0:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)
print(f"Your activation key is: {raw_activation_key}")


