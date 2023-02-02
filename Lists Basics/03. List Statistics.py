n = int(input())
positive_list = []
negative_list =[]
counter = 0
for i in range(n):
    number = int(input())
    if number >= 0:
        counter += 1
        positive_list.append(number)
    else:
        negative_list.append(number)
print(positive_list)
print(negative_list)
print(f"Count of positives: {counter}")
print(f"Sum of negatives: {sum(negative_list)}")
