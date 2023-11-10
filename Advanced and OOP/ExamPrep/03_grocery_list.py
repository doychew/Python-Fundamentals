def shop_from_grocery_list(budget, grocery_list, *product_and_price):
    all_products = []
    for product_name, price in product_and_price:
        if product_name not in grocery_list:
            continue
        if budget < float(price):
            break
        if product_name not in all_products:
            if float(price) <= budget:
                budget -= float(price)
                all_products.append(product_name)
                grocery_list.remove(product_name)
    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

