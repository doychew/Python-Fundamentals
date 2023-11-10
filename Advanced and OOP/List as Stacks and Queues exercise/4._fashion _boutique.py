clothes_stack = [int(x) for x in input().split()]
capacity_of_rack = int(input())
counter = 0
while clothes_stack:
    counter += 1
    current_rack_capacity = capacity_of_rack
    while clothes_stack and clothes_stack[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes_stack.pop()
print(counter)