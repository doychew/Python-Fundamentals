n = int(input())
stack = []
for i in range(n):
    data = input()
    splited_data = data.split()
    number_command = int(splited_data[0])
    if number_command == 1:
        number = int(splited_data[1])
        stack.append(number)
    elif number_command == 2:
        stack.pop()
    elif number_command == 3:
        print(max(stack))
    elif number_command == 4:
        print(min(stack))
while stack:
    print(stack.pop(), end="")
    if stack:
        print(", ", end="")