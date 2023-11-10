rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for i in range(rows)]
flat_matrix = []
for element in matrix:
    for el in element:
        flat_matrix.append(el)
print(flat_matrix)