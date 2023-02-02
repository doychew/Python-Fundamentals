list_of_integers = input().split()
numbers_to_remove = int(input())
list_of_integers_as_numbers = []

for element in list_of_integers:
    list_of_integers_as_numbers.append(int(element))
sorted_nums = sorted(list_of_integers_as_numbers)
for idx in range(numbers_to_remove):
    list_of_integers_as_numbers.remove(sorted_nums[idx])

filtered_list = list(map((lambda x: str(x)), list_of_integers_as_numbers))

print(', '.join(filtered_list))
