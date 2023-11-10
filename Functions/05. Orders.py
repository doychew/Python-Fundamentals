def shopping_list():
    if product == "coffee":
        return 1.50 * quantity
    elif product == "water":
        return 1.00 * quantity
    elif product == "coke":
        return 1.40 * quantity
    elif product == "snacks":
        return 2.00 * quantity
product = input()
quantity = int(input())
coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00
shopping_list()
print(f"{shopping_list():.2f}")