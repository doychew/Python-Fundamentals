def is_outside(row, col):
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return True


rows, cols = [int(x) for x in input().split()]
matrix = []
my_position_row = 0
my_position_col = 0
for i in range(rows):
    matrix.append(list(input()))
for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == "B":
            my_position_row, my_position_col = row, col

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}
current_row, current_col = my_position_row, my_position_col
while True:
    command = input()
    previous_row, previous_col = current_row, current_col
    current_row, current_col = directions[command](current_row, current_col)
    if is_outside(current_row, current_col):
        matrix[my_position_row][my_position_col] = " "
        print("The delivery is late. Order is canceled.")
        break
    if matrix[current_row][current_col] == "-":
        matrix[current_row][current_col] = "."
    if matrix[current_row][current_col] == "*":
        current_row, current_col = previous_row, previous_col
    if matrix[current_row][current_col] == "P":
        matrix[current_row][current_col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")
    if matrix[current_row][current_col] == "A":
        matrix[current_row][current_col] = "P"
        print("Pizza is delivered on time! Next order...")
        break
for el in matrix:
    print("".join(el))
