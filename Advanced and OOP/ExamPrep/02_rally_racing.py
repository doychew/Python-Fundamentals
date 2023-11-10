size_of_field = int(input())
race_number = input()
matrix = []
my_row = 0
my_col = 0
tunnel_coordinates = []
directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}
total_km_passed = 0
for i in range(size_of_field):
    matrix.append(input().split())
for row in range(size_of_field):
    for col in range(size_of_field):
        if matrix[row][col] == "T":
            tunnel_coordinates.append((row, col))

while True:
    command = input()

    if command == "End":
        print(f"Racing car {race_number} DNF.")
        matrix[my_row][my_col] = "C"
        break
    previous_row, previous_col = my_row, my_col
    my_row, my_col = directions[command](my_row, my_col)
    if matrix[my_row][my_col] == "T":
        matrix[my_row][my_col] = "."
        if (my_row, my_col) == tunnel_coordinates[0]:
            my_row, my_col = tunnel_coordinates[1]
            matrix[my_row][my_col] = "."
            total_km_passed += 30
        else:
            my_row, my_col = tunnel_coordinates[0]
            matrix[my_row][my_col] = "."
            total_km_passed += 30
    elif matrix[my_row][my_col] == ".":
        total_km_passed += 10
    elif matrix[my_row][my_col] == "F":
        matrix[my_row][my_col] = "C"
        total_km_passed += 10
        print(f"Racing car {race_number} finished the stage!")
        break
print(f"Distance covered {total_km_passed} km.")
for el in matrix:
    print(''.join(el))