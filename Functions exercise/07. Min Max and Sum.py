numbers = input().split()

all_nums = []
for element in numbers:
    all_nums.append((int(element)))
print(f"The minimum number is {min(all_nums)}")
print(f"The maximum number is {max(all_nums)}")
print(f"The sum number is: {sum(all_nums)}")