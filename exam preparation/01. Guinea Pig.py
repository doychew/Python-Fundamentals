import math
from math import ceil

enough_food = True
quantity_food_in_grams = float(input()) * 1000
quantity_hay_in_grams = float(input()) * 1000
quantity_cover_in_grams = float(input()) * 1000
puppy_weight_in_grams = float(input()) * 1000

for day in range(1, 31):
    quantity_food_in_grams -= 300

    if day % 2 == 0:
        quantity_hay_in_grams -= quantity_food_in_grams * 0.05

    if day % 3 == 0:
        quantity_cover_in_grams -= puppy_weight_in_grams / 3

    if quantity_food_in_grams <= 0 or quantity_cover_in_grams <= 0 or quantity_hay_in_grams <= 0:
        enough_food = False
        print("Merry must go to the pet store!")
        break


if enough_food:
    print(f"Everything is fine! Puppy is happy!"
          f" Food: {quantity_food_in_grams / 1000:.2f},"
          f" Hay: {quantity_hay_in_grams / 1000:.2f},"
          f" Cover: {(quantity_cover_in_grams / 1000):.2f}.")
