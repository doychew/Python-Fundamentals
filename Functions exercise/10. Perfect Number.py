def perfect_num(num):
    sum = 0
    for divisior in range(1, num):
        if num % divisior == 0:
            sum += divisior
    if sum == num:
        return "We have a perfect number!"
    return "It's not so perfect."





number = int(input())
print(perfect_num(number))
