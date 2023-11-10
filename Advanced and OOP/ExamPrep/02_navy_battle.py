size_of_the_field = int(input())
matrix = []
mines_hit = 0
destroyed_submarines = 0
submarine_row = 0
submarine_col = 0
directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}
for i in range(size_of_the_field):
    matrix.append(list(input()))

for row in range(size_of_the_field):
    for col in range(size_of_the_field):
        if matrix[row][col] == "S":
            submarine_row, submarine_col = row, col
current_row, current_col = submarine_row, submarine_col
while True:
    command = input()
    previous_row, previous_col = current_row, current_col
    current_row, current_col = directions[command](current_row, current_col)
    if matrix[current_row][current_col] == "-":
        matrix[current_row][current_col] = "S"
        matrix[previous_row][previous_col] = "-"
        continue
    if matrix[current_row][current_col] == "*":
        mines_hit += 1
        matrix[current_row][current_col] = "S"
        matrix[previous_row][previous_col] = "-"
        if mines_hit == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{current_row}, {current_col}]!")
            break
    if matrix[current_row][current_col] == "C":
        destroyed_submarines += 1
        matrix[current_row][current_col] = "S"
        matrix[previous_row][previous_col] = "-"
        if destroyed_submarines == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

for el in matrix:
    print(''.join(el))


