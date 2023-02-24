positive = []
negative = []
odd = []
even = []

numbers_list = []
numbers = input().split(", ")
for element in numbers:
    numbers_list.append(int(element))
    if int(element) >= 0:
        positive.append(element)
    else:
        negative.append(element)
    if int(element) % 2 == 0:
        even.append(element)
    else:
        odd.append(element)
print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")