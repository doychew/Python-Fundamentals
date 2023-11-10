rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split()] for i in range(rows)]
for col_index in range(cols):
    sum_elements = 0
    for row_index in range(rows):
        sum_elements += matrix[row_index][col_index]
    print(sum_elements)