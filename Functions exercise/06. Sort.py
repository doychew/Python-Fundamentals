numbers = input().split()
numbers_in_list = []
for element in numbers:
    numbers_in_list.append(int(element))
print(sorted(numbers_in_list))