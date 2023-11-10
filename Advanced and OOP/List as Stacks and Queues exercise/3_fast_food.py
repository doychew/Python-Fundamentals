from collections import deque
food_quantity = int(input())
orders_que = deque([int(x) for x in input().split()])
print(max(orders_que))
while orders_que and orders_que[0] <= food_quantity:
    food_quantity -= orders_que[0]
    orders_que.popleft()

if orders_que:
    print(f"Orders left: ", end="")
    while orders_que:
        print(f"{orders_que.popleft()}", end=" ")
else:
    print("Orders complete")