n = int(input())


for numbers in range(1, n + 1):
    it_is_special = False
    num_as_str = str(numbers)
    sum_digits = 0
    for char in num_as_str:
        sum_digits += int(char)

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        it_is_special = True
    print(f"{numbers} -> {it_is_special}")
