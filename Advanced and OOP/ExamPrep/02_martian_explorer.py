def is_outside(row, col):
    if row < 0 or row >= size_of_the_field or col < 0 or col >= size_of_the_field:
        return True


size_of_the_field = 6
matrix = []
rover_row = 0
rover_col = 0
for i in range(size_of_the_field):
    matrix.append(input().split())
for row in range(size_of_the_field):
    for col in range(size_of_the_field):
        if matrix[row][col] == "E":
            rover_row, rover_col = row, col
water_deposits = 0
metal_deposits = 0
concrete_deposits = 0
data = input().split(", ")

for command in data:
    if command == "up":
        rover_row -= 1
        if is_outside(rover_row, rover_col):
            rover_row = 5
    elif command == "down":
        rover_row += 1
        if is_outside(rover_row, rover_col):
            rover_row = 0
    elif command == "left":
        rover_col -= 1
        if is_outside(rover_row, rover_col):
            rover_col = 5
    elif command == "right":
        rover_col += 1
        if is_outside(rover_row, rover_col):
            rover_col = 0
    if matrix[rover_row][rover_col] == "W":
        print(f"Water deposit found at ({rover_row}, {rover_col})")
        water_deposits += 1
    elif matrix[rover_row][rover_col] == "M":
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
        metal_deposits += 1
    elif matrix[rover_row][rover_col] == "C":
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")
        concrete_deposits += 1
    elif matrix[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break
if water_deposits >= 1 and metal_deposits >= 1 and concrete_deposits >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
