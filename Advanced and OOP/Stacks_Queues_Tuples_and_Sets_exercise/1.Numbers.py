first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())
m = int(input())
for _ in range(m):
    data = input().split()
    command = data[0] + " " + data[1]
    numbers = [int(num) for num in data[2:]]
    if command == "Add First":
        first_sequence.update(numbers)
    elif command == "Add Second":
        second_sequence.update(numbers)
    elif command == "Remove First":
        first_sequence.difference_update(numbers)
    elif command == "Remove Second":
        second_sequence.difference_update(numbers)
    elif command == "Check Subset":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")