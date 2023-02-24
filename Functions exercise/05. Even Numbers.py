numbers = input().split()
integer_list = []
for element in numbers:
    if int(element) % 2 == 0:
        integer_list.append(int(element))



print(integer_list)