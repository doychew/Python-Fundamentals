def is_outside(row, col, matrix):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix):
        return True


def can_i_step(row, col, matrix):
    if matrix[row][col] == ".":
        return True


targets = 0
size_of_the_field = 5
matrix = []
my_position_row = 0
my_position_col = 0
for i in range(size_of_the_field):
    matrix.append([x for x in input().split()])
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "A":
            my_position_row, my_position_col = row, col
        elif matrix[row][col] == "x":
            targets += 1
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
targets_down = []
count_of_commands = int(input())
for _ in range(count_of_commands):
    command = input().split()
    if command[0] == "shoot":
        current_row = my_position_row + directions[command[1]][0]
        current_col = my_position_col + directions[command[1]][1]
        while not is_outside(current_row, current_col, matrix):
            if matrix[current_row][current_col] == "x":
                matrix[current_row][current_col] = "."
                targets -= 1
                targets_down.append([current_row, current_col])
                break
            current_row += directions[command[1]][0]
            current_col += directions[command[1]][1]
        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break
    elif command[0] == "move":
        steps = int(command[2])
        direction = command[1]
        if direction == "up":
            current_row = my_position_row - steps
            current_col = my_position_col
        elif direction == "down":
            current_row = my_position_row + steps
            current_col = my_position_col
        elif direction == "left":
            current_row = my_position_row
            current_col = my_position_col - steps
        else:
            current_row = my_position_row
            current_col = my_position_col + steps
        if not is_outside(current_row, current_col, matrix) and can_i_step(current_row, current_col, matrix):
            matrix[current_row][current_col] = "A"
            matrix[my_position_row][my_position_col] = "."
            my_position_row, my_position_col = current_row, current_col
if targets > 0:
    print(f"Training not completed! {targets} targets left.")
for element in targets_down:
    print(element)

