def is_outside(row, col, matrix):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix):
        return True


def is_trap(row, col, matrix):
    if matrix[row][col] == "R":
        return True


n = int(input())
matrix = []
alice_row = 0
alice_col = 0
tea_bags = 0

directions = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1)
}
for i in range(n):
    matrix.append([x for x in input().split()])
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "A":
            alice_row, alice_col = row, col
            matrix[row][col] = "*"
current_row, current_col = alice_row, alice_col
while tea_bags <= 10:
    command = input()
    current_row, current_col = directions[command](current_row, current_col)
    if is_outside(current_row, current_col, matrix):
        break
    if is_trap(current_row, current_col, matrix):
        matrix[current_row][current_col] = "*"
        break
    if matrix[current_row][current_col] == "." or matrix[current_row][current_col] == "*":
        matrix[current_row][current_col] = "*"
        continue
    tea_bags += int(matrix[current_row][current_col])
    if tea_bags >= 10:
        matrix[current_row][current_col] = "*"
        break
    matrix[current_row][current_col] = "*"

if tea_bags >= 10:
    print(f"She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for element in matrix:
    print(*element)
