import json
import os
import tkinter as tk
from canvas import app
from helpers import cleans_screen
from PIL import Image, ImageTk

base_path = os.path.dirname(__file__)


def buy_product(p):
    pass


def render_products_screen():
    cleans_screen()

    with open("db/current_users.txt") as f:
        username = f.read()
    # with open("db/users.txt") as f:
    #     users = [json.loads(u.strip()) for u in f]
    #     for user in users:
    #         if user["username"] == username:
    with open("db/products.txt") as f:
        products = [json.loads(p.strip()) for p in f]
        for i, product in enumerate(products):
            row = i // 4 * 4
            column = i % 4
            tk.Label(app, text=product["name"]).grid(row=row, column=column)

            img = Image.open(os.path.join(base_path, "db/images", product["img_path"])).resize((100, 100))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(image=photo_image)
            image_label.image = photo_image
            image_label.grid(row=row + 1, column=column)

            tk.Label(app, text=product["count"]).grid(row=row + 2, column=column)
            tk.Button(app,
                      text=f"Buy {product['id']}",
                      command=lambda p=product["id"]: buy_product(p)
                      ).grid(row=row + 3, column=column)
