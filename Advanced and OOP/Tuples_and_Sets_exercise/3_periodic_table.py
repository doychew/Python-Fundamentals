n = int(input())
unique_elements = set()
for _ in range(n):
    chemicals = input().split()
    for element in chemicals:
        unique_elements.add(element)

print("\n".join(unique_elements))