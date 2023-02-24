def factorial(number):
    result = 1
    for current_number in range(1, number + 1):
        result *= current_number
    return result


first_num = int(input())
second_num = int(input())
first_num_factorial = factorial(first_num)
second_num_num_factorial = factorial(second_num)
final_result = first_num_factorial / second_num_num_factorial
print(f"{final_result:.2f}")
