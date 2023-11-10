numbers = [int(x) for x in input().split()]
negative = []
positive = []
for el in numbers:
    if el < 0:
        negative.append(el)
    elif el >= 0:
        positive.append(el)
print(sum(negative))
print(sum(positive))
if abs(sum(negative)) > sum(positive):
    print(f"The negatives are stronger than the positives")
elif sum(positive) > abs(sum(negative)):
    print(f"The positives are stronger than the negatives")