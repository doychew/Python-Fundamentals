def is_outside(row_index, col_index, matrix):
    if row_index < 0 or row_index >= len(matrix) or col_index < 0 or col_index >= len(matrix):
        return True


size_of_the_field = int(input())
matrix = []
bunny_row = 0
bunny_col = 0
best_direction = ""
best_path = ""
max_eggs = float("-inf")
directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}
for i in range(size_of_the_field):
    matrix.append(input().split())
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "B":
            bunny_row, bunny_col = row, col
for direction, step in directions.items():
    current_row, current_col = bunny_row, bunny_col
    current_eggs = 0
    current_path = []
    current_direction = direction
    while True:
        current_row, current_col = step(current_row, current_col)
        if is_outside(current_row, current_col, matrix):
            break
        if matrix[current_row][current_col] == "X":
            break
        current_eggs += int(matrix[current_row][current_col])
        current_path.append([current_row, current_col])
    if current_eggs >= max_eggs:
        max_eggs = current_eggs
        best_path = current_path
        best_direction = current_direction
print(best_direction)
for element in best_path:
    print(element)
print(max_eggs)


