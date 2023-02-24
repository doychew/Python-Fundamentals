total_price_without_taxes = 0
taxes = 0
final_price = 0
discount = 0
while True:
    command = input()
    if command == "special" or command == "regular":
        break

    current_prices = float(command)
    if current_prices < 0:
        print("Invalid price!")
        continue

    total_price_without_taxes += current_prices
    taxes += current_prices * 0.2
final_price += total_price_without_taxes + taxes
if final_price == 0:
    print("Invalid order!")
else:
    if command == "special":
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price_without_taxes:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {final_price - (final_price * 0.1):.2f}$")
    else:
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price_without_taxes:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {final_price:.2f}$")


