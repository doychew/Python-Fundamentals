sequence_numbers = input().split()
int_numbers = []
for element in sequence_numbers:
    if int(element) % 2 == 0:
        int_numbers.append(int(element))
print(int_numbers)
