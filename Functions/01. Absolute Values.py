list_in_string = input().split()
numbers_as_string = []
for element in list_in_string:
    numbers_as_string.append(abs(float(element)))
print(numbers_as_string)

