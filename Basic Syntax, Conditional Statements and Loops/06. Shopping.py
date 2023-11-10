budget = int(input())
while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    prices = int(command)
    budget -= prices
    if budget < 0:
        print("You went in overdraft!")
        break
