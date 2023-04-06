possible_messages = int(input())
people = {}

while True:
    input_str = input()
    if input_str == "Statistics":
        break

    command = input_str.split("=")
    action = command[0].strip()

    if action == "Add":
        user_name = command[1].strip()
        sent_messages = int(command[2].strip())
        received_messages = int(command[3].strip())
        if user_name not in people:
            people[user_name] = [sent_messages, received_messages]

    elif action == "Message":
        sender = command[1].strip()
        receiver = command[2].strip()

        if sender in people and receiver in people:
            people[sender][0] += 1
            people[receiver][1] += 1
            if people[sender][0] + people[sender][1] >= possible_messages:
                print(f"{sender} reached the capacity!")
                del people[sender]

            if people[receiver][0] + people[receiver][1] >= possible_messages:
                print(f"{receiver} reached the capacity!")
                del people[receiver]

    elif action == "Empty":
        username = command[1].strip()
        if username in people:
            del people[username]
        if username == "All":
            people.clear()

print(f"Users count: {len(people)}")

for username, messages in people.items():
    calculation = messages[0] + messages[1]
    print(f"{username} - {calculation}")