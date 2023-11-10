def is_outside(row, col):
    if row < 0 or row >= size_of_the_field or col < 0 or col >= size_of_the_field:
        return True


size_of_the_field = int(input())
matrix = []
my_row = 0
my_col = 0
fish_kilograms = 0
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
            my_row, my_col = row, col
get_into_whirlpool = False
command = input()
current_row, current_col = my_row, my_col
while command != "collect the nets":
    previous_row, previous_col = current_row, current_col
    current_row, current_col = directions[command](current_row, current_col)
    if is_outside(current_row, current_col):
        if command == "up":
            current_row = size_of_the_field - 1
        elif command == "down":
            current_row = 0
        elif command == "right":
            current_col = 0
        elif command == "left":
            current_col = size_of_the_field - 1
    if matrix[current_row][current_col] == "-":
        continue
    elif matrix[current_row][current_col] == "W":
        fish_kilograms = 0
        print(f"You fell into a whirlpool!"
              f" The ship sank and you lost the fish you caught. Last coordinates of the ship: [{current_row},{current_col}]")
        get_into_whirlpool = True
        break
    elif matrix[current_row][current_col].isdigit()
        
    command = input()
if fish_kilograms >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota!"
          f"You need {20 - fish_kilograms} tons of fish more.")
if fish_kilograms > 0:
    print(f"Amount of fish caught: {fish_kilograms} tons.")
if get_into_whirlpool == False:
    for el in matrix:
        print("".join(el))


