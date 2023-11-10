numbers = input().split(", ")
positive = []
negative = []
even = []
odd = []
number_list = []
for element in numbers:
    number_list.append(int(element))
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
