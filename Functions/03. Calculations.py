command = input()
first_num = int(input())
second_num = int(input())
def calculate():
    if command == "multiply":
        return first_num * second_num
    elif command == "divide":
        return first_num // second_num
    elif command == "add":
        return first_num + second_num
    elif command == "subtract":
        return first_num - second_num
calculate()
print(calculate())
