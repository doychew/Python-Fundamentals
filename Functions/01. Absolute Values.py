sequence_numbers = input().split()
numbers_as_list = []
for element in sequence_numbers:
    numbers_as_list.append(abs(float(element)))
print(numbers_as_list)