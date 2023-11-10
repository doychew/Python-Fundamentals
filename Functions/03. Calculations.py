def calculation():
    if command == "subtract":
        result = first_num - second_num
    elif command == "divide":
        result = first_num // second_num
    elif command == "add":
        result = first_num + second_num
    elif command == "multiply":
        result = first_num * second_num
    return result
command = input()
first_num = int(input())
second_num = int(input())
print(calculation())
