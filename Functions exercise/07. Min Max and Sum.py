sequence = input().split()
calculations = []
for element in sequence:
    calculations.append(int(element))
minimum_number = min(calculations)
max_number = max(calculations)
sum_of_numbers = sum(calculations)
print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_of_numbers}")