numbers = tuple([x for x in input().split()])
occ = {}
for i in numbers:
    occ[i] = numbers.count(i)

for key, value in occ.items():
    print(f"{key} - {value} times")