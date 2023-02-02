factor = int(input())
count = int(input())
lenght_count = []
for i in range(factor, factor * count + 1, factor):
    lenght_count.append(i)
print(lenght_count)