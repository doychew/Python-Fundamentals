rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for i in range(rows)]
counter = 0
for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        down_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]
        if current_element == next_element == diagonal_element == down_element:
            counter += 1
print(counter)