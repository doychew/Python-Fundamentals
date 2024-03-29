from collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while bowls_of_ramen and customers:
    current_ramen = bowls_of_ramen.pop()
    current_customer = customers.popleft()
    if current_ramen == current_customer:
        continue
    elif current_ramen > current_customer:
        current_ramen -= current_customer
        bowls_of_ramen.append(current_ramen)
    elif current_customer > current_ramen:
        current_customer -= current_ramen
        customers.appendleft(current_customer)
if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls_of_ramen))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str, customers))}")