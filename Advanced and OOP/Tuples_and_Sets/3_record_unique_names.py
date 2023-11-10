n = int(input())
unique_names = []
for _ in range(n):
    name = input()
    unique_names.append(name)
print('\n'.join(set(unique_names)))