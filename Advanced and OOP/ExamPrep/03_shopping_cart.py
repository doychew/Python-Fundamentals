def shopping_cart(*args):
    pizza_dict = {}
    soup_dict = {}
    desert_dict = {}
    for info in args:
        meal_type = args[0]
        product = args[1]
        if args == "Stop":
            break
        if meal_type == "Pizza":
            if product not in pizza_dict:
                pizza_dict[meal_type] += product
        elif meal_type == "Soup":
            if product not in soup_dict:
                soup_dict[meal_type] += product
        elif meal_type == "Dessert":
            if product not in desert_dict:
                desert_dict[meal_type] += product

