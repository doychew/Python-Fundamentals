employees_happines = input().split()
factor = int(input())
multiply_happines = []
for element in employees_happines:
    multiply_happines.append(int(element))
filtered = list(filter(lambda x: x >= (sum(multiply_happines) / len(multiply_happines)), multiply_happines))
if len(filtered) >= len(multiply_happines) / 2:
    print(f"Score: {len(filtered)}/{len(multiply_happines)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(multiply_happines)}. Employees are not happy!")