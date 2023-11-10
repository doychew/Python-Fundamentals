n = int(input())
sum = 0
matrix = [[int(x) for x in input().split()] for i in range(n)]
for row_index in range(n):
    sum += matrix[row_index][row_index]
print(sum)