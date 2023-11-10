rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")]for i in range(rows)]
sub_matrix = []
max_sum = float('-inf')
for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        down_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]
        sum_elements = current_element + next_element + down_element + diagonal_element

        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [[current_element, next_element], [down_element, diagonal_element]]
print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)