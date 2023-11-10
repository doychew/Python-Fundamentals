def calculation(number):
    odd = 0
    even = 0
    for current_number in number:
        if int(current_number) % 2 == 0:
            even += int(current_number)
        else:
            odd += int(current_number)
    return odd, even

number_as_string = input()
odd, even = calculation(number_as_string)
print(f"Odd sum = {odd}, Even sum = {even}")
