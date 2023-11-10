def is_outside(row, col):
    if row < 0 or row >= size_of_the_field or col < 0 or col >= size_of_the_field:
        return True


is_game_over = False
size_of_the_field = int(input())
matrix = []
collected_hazelnuts = 0
possible_moves = input().split(", ")
squirrel_row = 0
squirrel_col = 0

for row in range(size_of_the_field):
    matrix.append(list(input()))
    for col in range(size_of_the_field):
        if matrix[row][col] == "s":
            squirrel_row, squirrel_col = row, col

for direction in possible_moves:
    matrix[squirrel_row][squirrel_col] = "*"
    if direction == "up":
        squirrel_row -= 1
    elif direction == "down":
        squirrel_row += 1
    elif direction == "left":
        squirrel_col -= 1
    elif direction == "right":
        squirrel_col += 1

    if not (0 <= squirrel_row < size_of_the_field and 0 <= squirrel_col < size_of_the_field):
        print("The squirrel is out of the field.")
        is_game_over = True
        break

    if matrix[squirrel_row][squirrel_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        is_game_over = True
        break

    if matrix[squirrel_row][squirrel_col] == "h":
        collected_hazelnuts += 1
        if collected_hazelnuts == 3:
            is_game_over = True
            print("Good job! You have collected all hazelnuts!")
            break

if collected_hazelnuts < 3 and not is_game_over:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {collected_hazelnuts}")
