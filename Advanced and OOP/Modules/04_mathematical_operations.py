row, col = [int(x) for x in input().split()]
matrix = []
for i in range(row):
    matrix.append(int(i))
for j in range(col):
    matrix.append(int(j))
print(matrix)