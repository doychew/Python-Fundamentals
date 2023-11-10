def even_odd(*args):
    command = args[-1]
    even = []
    odd = []
    for el in args[:-1]:
        if int(el) % 2 == 0:
            even.append(el)
        else:
            odd.append(el)
    if command == "odd":
        return odd
    else:
        return even

print(even_odd(1, 2, 3, 4, 5, 6, 55, 110, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55, 111, "odd"))