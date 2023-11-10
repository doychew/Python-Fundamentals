numbers = input().split(", ")
even_numbers = [int(element) for element in range(len(numbers)) if numbers[element] % 2 == 0]
print(even_numbers)