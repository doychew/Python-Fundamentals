def smallest_number():
    if first_num < second_num and first_num < third_num:
        return first_num
    elif second_num < first_num and second_num < third_num:
        return second_num
    else:
        return third_num
first_num = int(input())
second_num = int(input())
third_num = int(input())
print(smallest_number())