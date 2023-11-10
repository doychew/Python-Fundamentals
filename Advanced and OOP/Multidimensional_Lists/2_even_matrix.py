rows = int(input())
sub_matrix = []
matrix = []
for i in range(rows):
    element = [int(x) for x in input().split(", ")]
    matrix.append(element)
for row_index in range(rows):
    sub_matrix.append([])
    for col_index in range(len(matrix[row_index])):
        current_element = matrix[row_index][col_index]
        if current_element % 2 ==0:
            sub_matrix[row_index].append(current_element)
print(sub_matrix)