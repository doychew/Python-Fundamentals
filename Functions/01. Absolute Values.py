numbers = input().split()
new_list = []
for element in numbers:
    new_list.append(abs(float(element)))
print(new_list)