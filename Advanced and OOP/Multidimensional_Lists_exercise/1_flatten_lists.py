numbers = input().split("|")
matrix = []
for i in range(len(numbers) -1 ,-1 ,-1):
    row = [int(x) for x in numbers[i].split()]
    if row:
        matrix.append(row)
for row in matrix:
    print(*row, sep=" ", end=" ")