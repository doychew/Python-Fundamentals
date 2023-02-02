command = input()
quantity = int(input())
total_sum = 0
money_counter = 0


def final_sum():
    total_sum = 0
    money_counter = 0
    if command == "water":
        money_counter += 1.00
    elif command == "coffee":
        money_counter += 1.50
    elif command == "coke":
        money_counter += 1.40
    elif command == "snacks":
        money_counter += 2.00
    total_sum = quantity * money_counter
    return total_sum


print(f"{final_sum():.2f}")
