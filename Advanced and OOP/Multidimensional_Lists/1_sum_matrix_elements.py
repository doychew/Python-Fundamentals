matrix = []
sum_numbers = 0
rows, cols = [int(x) for x in input().split(", ")]
for row in range(rows):
    element = [int(x) for x in input().split(", ")]
    sum_numbers += sum(element)
    matrix.append(element)

print(sum_numbers)
print(matrix)