def is_outside(row_, col_):
    if row_ < 0 or row_ >= int(row_of_the_field) or col_ < 0 or col_ >= int(col_of_the_field):
        return True


row_of_the_field, col_of_the_field = input().split()
matrix = []
my_row = 0
my_col = 0
moves = 0
other_players = 3
other_players_caught = 0
directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}
for i in range(int(row_of_the_field)):
    matrix.append(input().split())
for row in range(int(row_of_the_field)):
    for col in range(int(col_of_the_field)):
        if matrix[row][col] == "B":
            my_row, my_col = row, col
current_row, current_col = my_row, my_col
while True:
    command = input()
    if command == "Finish":
        break
    previous_row, previous_col = current_row, current_col
    current_row, current_col = directions[command](current_row, current_col)
    if is_outside(current_row, current_col):
        current_row, current_col = previous_row, previous_col
    if matrix[current_row][current_col] == "O":
        current_row, current_col = previous_row, previous_col
    if matrix[current_row][current_col] == "-":
        moves += 1
        matrix[current_row][current_col] = "B"
        matrix[previous_row][previous_col] = "-"
    if matrix[current_row][current_col] == "P":
        moves += 1
        other_players_caught += 1
        matrix[current_row][current_col] = "B"
        matrix[previous_row][previous_col] = "-"
    if other_players_caught == 3:
        break
print("Game over!")
print(f"Touched opponents: {other_players_caught} Moves made: {moves}")
