sequence = input().split()
int_numbers = []
for element in sequence:
    int_numbers.append(int(element))
result = sorted(int_numbers)
print(result)