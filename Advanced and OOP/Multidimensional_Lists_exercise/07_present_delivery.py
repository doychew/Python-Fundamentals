number_of_presents = int(input())
size = int(input())
matrix = []
count_happy_kids = 0
all_happy_kids = 0
santa_row = 0
santa_col = 0
for i in range(size):
    matrix.append(input().split())
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            matrix[row][col] = "-"
            santa_row = row
            santa_col = col
        if matrix[row][col] == "V":
            all_happy_kids += 1
            count_happy_kids += 1

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}
current_row, current_col = santa_row, santa_col
while True:
    command = input()
    if command == "Christmas morning":
        break
    current_row, current_col = directions[command](current_row, current_col)
    if matrix[current_row][current_col] == "X":
        matrix[current_row][current_col] = "-"
        continue
    if matrix[current_row][current_col] == "V":
        number_of_presents -= 1
        count_happy_kids -= 1
        matrix[current_row][current_col] = "-"
    if matrix[current_row][current_col] == "C":

        for direction, step in directions.items():
            cookie_row, cookie_col = current_row, current_col
            cookie_row, cookie_col = step(cookie_row, current_col)
            if matrix[cookie_row][cookie_col] == "V":
                number_of_presents -= 1
                count_happy_kids -= 1
                matrix[cookie_row][cookie_col] = "-"
            if matrix[cookie_row][cookie_col] == "X":
                number_of_presents -= 1
                matrix[cookie_row][cookie_col] = "-"
    if number_of_presents == 0:
        break
    if matrix[current_row][current_col] == "-":
        continue
matrix[current_row][current_col] = "S"

if number_of_presents == 0 and count_happy_kids > 0:
    print("Santa ran out of presents!")
for el in matrix:
    print(*el)
if count_happy_kids == 0:
    print(f"Good job, Santa! {all_happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {count_happy_kids} nice kid/s.")
