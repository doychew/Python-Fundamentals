n = int(input())
matrix = [[x for x in input()]for i in range(n)]
searched_element = input()
position = None
for row_index in range(n):
    if position:
        break
    for col_index in range(len(matrix[row_index])):
        current_element = matrix[row_index][col_index]
        if current_element == searched_element:
            position = (row_index, col_index)
            print(position)
            break

if not position:
    print(f"{searched_element} does not occur in the matrix")