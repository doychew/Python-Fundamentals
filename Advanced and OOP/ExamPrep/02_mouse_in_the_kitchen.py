def is_outside(row, col):
    if row < 0 or row >= rows_count or col < 0 or col >= cols_count:
        return True


rows_count, cols_count = [int(x) for x in input().split(",")]

matrix = []
total_cheese_count = 0
mouse_row = 0
mouse_col = 0


direction_mapper = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}
for i in range(rows_count):
    matrix.append(list(input()))
for row in range(rows_count):
    for col in range(cols_count):
        if matrix[row][col] == "M":
            mouse_row, mouse_col = row, col
        if matrix[row][col] == "C":
            total_cheese_count += 1


current_row, current_col = mouse_row, mouse_col
eaten_cheese = 0
while True:
    direction = input()
    if direction == "danger":
        print("Mouse will come back later!")
        break
    previous_row, previous_col = current_row, current_col
    current_row, current_col = direction_mapper[direction](current_row, current_col)

    if is_outside(current_row, current_col):
        print("No more cheese for tonight!")
        matrix[previous_row][previous_col] = "M"
        matrix[mouse_row][mouse_col] = "*"
        break

    if matrix[current_row][current_col] == "*":
        continue

    if matrix[current_row][current_col] == "C":
        matrix[current_row][current_col] = "M"
        matrix[mouse_row][mouse_col] = "*"
        eaten_cheese += 1
        mouse_row, mouse_col = [current_row, current_col]

        if eaten_cheese == total_cheese_count:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    if matrix[current_row][current_col] == "T":
        matrix[current_row][current_col] = "M"
        matrix[mouse_row][mouse_col] = "*"
        print("Mouse is trapped!")
        break

    if matrix[current_row][current_col] == "@":
        current_row, current_col = previous_row, previous_col
        continue
for el in matrix:
    print("".join(el))
