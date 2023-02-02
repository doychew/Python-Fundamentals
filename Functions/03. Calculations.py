def calculate(command, num, num1):
    result = 0
    if command == "subtract":
        result = num - num1
    elif command == "multiply":
        result = num * num1
    elif command == "divide":
        result = num // num1
    elif command == "add":
        result = num + num1
    return result


command_operator = input()
first_num = int(input())
second_num = int(input())
print(calculate(command_operator, first_num, second_num))
