first_num = int(input())
second_num = int(input())
third_num = int(input())
all_numbers = [first_num, second_num, third_num]


def smallest_num():
    return min(all_numbers)


print(smallest_num())
